# -*- coding: utf-8 -*-
"""Application layers"""

import os
import math
import re
from collections import defaultdict

from qgis.core import *
from PyQt4.QtCore import QVariant

import hgwnames
import setup
import logging
log = logging.getLogger(setup.app_name + "." + __name__)

is_inside = lambda f1, f2: \
    f2.geometry().contains(f1.geometry()) or f2.geometry().overlaps(f1.geometry())

get_attributes = lambda feat: \
    dict([(i, feat[i]) for i in range(len(feat.fields().toList()))])
    
    
class Point(QgsPoint):
    """Extends QgsPoint with some utility methods"""

    def __init__(self, arg1, arg2=None):
        if arg2 is None:
            try:
                super(Point, self).__init__(arg1[0], arg1[1])
            except:
                super(Point, self).__init__(arg1)
        else:
            super(Point, self).__init__(arg1, arg2)
    
    def boundingBox(self, radius):
        """Returns a bounding box of 2*radius centered in point."""
        return QgsRectangle(self.x() - radius, self.y() - radius,
                        self.x() + radius, self.y() + radius)

    def get_angle_with_context(self, geom, acute_thr=setup.acute_thr,
            straight_thr=setup.straight_thr, cath_thr=setup.dist_thr):
        """
        For the vertex in a geometry nearest to this point, give the angle 
        between its adjacent vertexs.
        
        Args:
            geom (QgsGeometry): Geometry to test.
            acute_thr (float): Acute angle threshold.
            straight_thr (float): Straight angle threshold.
            cath_thr (float): Cathetus threshold.
        
        Returns:
            (float) Angle between the vertex and their adjacents,
            (bool)  True for a corner (the angle differs by more than straight_thr
            of 180 and if the distance from the vertex to the segment formed by 
            their adjacents is greater than cath_thr.
            (bool)  True if the angle is too low (< acute_thr)
            (float) Distance from the vertex to the segment formed by their adjacents
        """
        (point, ndx, ndxa, ndxb, dist) = geom.closestVertex(self)
        va = geom.vertexAt(ndxa) # previous vertex
        vb = geom.vertexAt(ndxb) # next vertex
        angle = abs(point.azimuth(va) - point.azimuth(vb))
        a = abs(va.azimuth(point) - va.azimuth(vb))
        h = math.sqrt(va.sqrDist(point))
        c = abs(h * math.sin(math.radians(a)))
        is_corner = abs(180 - angle) > straight_thr and c > cath_thr
        is_acute = angle < acute_thr if angle < 180 else 360 - angle < acute_thr
        return (angle, is_acute, is_corner, c)


class BaseLayer(QgsVectorLayer):
    """Base class for application layers"""

    def __init__(self, path, baseName, providerLib = "ogr"):
        super(BaseLayer, self).__init__(path, baseName, providerLib)
        self.writer = self.dataProvider()
        self.rename={}
        self.resolve={}
        self.reference_matchs={}
    
    def copy_feature(self, feature, rename=None, resolve=None):
        """
        Return a copy of feature renaming attributes or resolving xlink references.

        Args:
            feature (QgsFeature): Source feature
            rename (dict): Translation of attributes names
            resolve (dict): xlink reference fields

        Examples:
            With this:
            
            >>> rename = {'spec': 'specification'}
            >>> resolve = {
            ...     'PD_id': ('component_href', '[\w\.]+PD[\.0-9]+'), 
            ...     'TN_id': ('component_href', '[\w\.]+TN[\.0-9]+'), 
            ...     'AU_id': ('component_href', '[\w\.]+AU[\.0-9]+')
            ... }
                
            You get:
            
            >>> original_attributes = ['localId', 'specification', 'component_href']
            >>> original_values = [
            ...     '38.012.1.12.0295603CS6109N', 
            ...     'Parcel', 
            ...     '(3:#ES.SDGC.PD.38.012.38570,#ES.SDGC.TN.38.012.1,#ES.SDGC.AU.38.012)'
            ... ]
            >>> final_attributes = ['localId', 'spec', 'PD_id', 'TN_id', 'AU_id']
            >>> final_values = [
            ...     '38.012.1.12.0295603CS6109N', 
            ...     'Parcel', 
            ...     'ES.SDGC.PD.38.012.38570',  
            ...     'ES.SDGC.TN.38.012.1',
            ...     'ES.SDGC.AU.38.012'
            ... ]
        """
        rename = rename if rename is not None else self.rename
        resolve = resolve if resolve is not None else self.resolve
        if self.pendingFields().isEmpty():
            self.dataProvider().addAttributes(feature.fields().toList())
            self.updateFields()
        dst_ft = QgsFeature(self.pendingFields())
        dst_ft.setGeometry(feature.geometry())
        src_attrs = [f.name() for f in feature.fields()]
        for field in self.pendingFields().toList():
            dst_attr = field.name()
            if dst_attr in resolve:
                (src_attr, reference_match) = resolve[dst_attr]
                match = re.search(reference_match, feature[src_attr])
                if match:
                    dst_ft[dst_attr] = match.group(0)
            else:
                src_attr = dst_attr
                if dst_attr in rename:
                    src_attr = rename[dst_attr]
                if src_attr in src_attrs:
                    dst_ft[dst_attr] = feature[src_attr]
        return dst_ft
    
    def append(self, layer, rename=None, resolve=None, query=None, **kwargs):
        """Copy all features from layer.

        Args:
            layer (QgsVectorLayer): Source layer
            rename (dict): Translation of attributes names
            resolve (dict): xlink reference fields
            query (func): function with args feature and kwargs that returns
                a boolean deciding if each feature will be included or not
            kwargs: aditional arguments for query function

        Examples:

            >>> query = lambda feat, kwargs: feat['foo']=='bar'
            Will copy only features with a value 'bar' in the field 'foo'.
            >>> query = lambda feat, kwargs: layer.is_inside(feat, kwargs['zone'])
            Will copy only features inside zone.
            
            See also copy_feature().
        """
        self.setCrs(layer.crs())
        to_add = []
        for feature in layer.getFeatures():
            if not query or query(feature, kwargs):
                to_add.append(self.copy_feature(feature, rename, resolve))
        if to_add:
            self.startEditing()
            self.addFeatures(to_add)
            self.commitChanges()
            log.debug (_("Loaded %d features in '%s' from '%s'"), len(to_add),
                self.name().encode('utf-8'), layer.name().encode('utf-8'))

    def reproject(self, target_crs=None):
        """Reproject all features in this layer to a new CRS.

        Args:
            target_crs (QgsCoordinateReferenceSystem): New CRS to apply.
        """
        if target_crs is None:
            target_crs = QgsCoordinateReferenceSystem(4326)
        crs_transform = QgsCoordinateTransform(self.crs(), target_crs)
        to_add = []
        to_clean = []
        for feature in self.getFeatures():
            geom = feature.geometry()
            geom.transform(crs_transform)
            out_feat = QgsFeature()
            out_feat.setGeometry(geom)
            out_feat.setAttributes(feature.attributes())
            to_add.append(out_feat)
            to_clean.append(feature.id())
        self.startEditing()
        self.writer.deleteFeatures(to_clean)
        self.writer.addFeatures(to_add)
        self.setCrs(target_crs)
        self.commitChanges()
        self.updateExtents()
        log.debug(_("Reprojected the '%s' layer to '%s' CRS"), 
            self.name().encode('utf-8'), target_crs.description())
    
    def join_field(self, source_layer, target_field_name, join_field_name, 
            field_names_subset, prefix = ""):
        """
        Replaces qgis table join mechanism becouse I'm not able to work with it 
        in standalone script mode (without GUI).
        
        Args:
            source_layer (QgsVectorLayer): Source layer.
            target_field_name (str): Join field in the target layer. 
            join_fieldsName (str): Join field in the source layer.
            field_names_subset (list): List of field name strings for the target layer.
            prefix (str): An optional prefix to add to the target fields names
        """
        fields = []
        target_attrs = [f.name() for f in self.pendingFields()]
        for attr in field_names_subset:
            field = source_layer.pendingFields().field(attr)
            if field.length > 254:
                field.setLength(254)
            field.setName(prefix + attr)
            if field.name() not in target_attrs:
                fields.append(field)
        self.writer.addAttributes(fields)
        self.updateFields()
        source_values = {}
        for feature in source_layer.getFeatures():
            source_values[feature[join_field_name]] = \
                    {attr: feature[attr] for attr in field_names_subset}
        to_change = {}
        for feature in self.getFeatures():
            attrs = {}
            for attr in field_names_subset:
                fieldId = feature.fieldNameIndex(prefix + attr)
                value = None
                if feature[target_field_name] in source_values:
                    value = source_values[feature[target_field_name]][attr]
                attrs[fieldId] = value 
            to_change[feature.id()] = attrs
        if to_change:
            self.startEditing()
            self.writer.changeAttributeValues(to_change)
            self.commitChanges()
            log.debug(_("Joined '%s' to '%s'"), source_layer.name().encode('utf-8'),
                self.name().encode('utf-8'))

    def translate_field(self, field_name, translations, clean=True):
        """
        Transform the values of a field
        
        Args:
            field_name (str): Name of the field to transform
            translations (dict): A dictionary used to transform field values
            clean (bool): If true (default), delete features without translation
        """
        field_ndx = self.pendingFields().fieldNameIndex(field_name)
        if field_ndx >= 0:
            to_clean = []
            to_change = {}
            for feat in self.getFeatures():
                value = feat[field_name]
                if value in translations and translations[value] != '':
                    new_value = translations[value]
                    attributes = get_attributes(feat)
                    attributes[field_ndx] = new_value
                    to_change[feat.id()] = attributes
                elif clean:
                    to_clean.append(feat.id())
            self.startEditing()
            self.writer.changeAttributeValues(to_change)
            self.writer.deleteFeatures(to_clean)
            self.commitChanges()

    def export(self, path, driver_name="ESRI Shapefile", overwrite=True):
        """Write layer to file

        Args:
            path (str): Path of the output file
            driver_name (str): Defaults to ESRI Shapefile.
            overwrite (bool): Defaults to True
        """
        if os.path.exists(path) and overwrite:
            if driver_name == 'ESRI Shapefile':
                QgsVectorFileWriter.deleteShapeFile(path)
            else:
                os.remove(path)
        return QgsVectorFileWriter.writeAsVectorFormat(self, path, "utf-8", 
                self.crs(), driver_name) == QgsVectorFileWriter.NoError

    def search(self, expression):
        """Returns a features list for this search expression
        """
        exp = QgsExpression(expression)
        request = QgsFeatureRequest(exp)
        return self.getFeatures(request)

    def get_child_features(self, child_layer):
        """Returns a dictionary of lists with the features in child_layer
        contained in each feature of this layer

        Args:
            child_layer (QgsVectorLayer): Layer that is contained
        """
        child_features = {}
        for f1 in self.getFeatures():
            child_features[f1.id()] = []
            for f2 in child_layer.getFeatures():
                if f2.id() not in child_features[f1.id()] and is_inside(f2, f1):
                    child_features[f1.id()].append(f2.id())
        return child_features


class PolygonLayer(BaseLayer):
    """Base class for polygon layers"""

    def __init__(self, path, baseName, providerLib = "ogr"):
        super(PolygonLayer, self).__init__(path, baseName, providerLib)
        self.dup_thr = setup.dup_thr # Distance in meters to merge nearest vertex.
        self.cath_thr = setup.dist_thr # Threshold in meters for cathetus reduction
        self.straight_thr = setup.straight_thr # Threshold in degrees from straight angle to delete a vertex
        self.dist_thr = setup.dist_thr # Threshold for topological points.

    def explode_multi_parts(self):
        """
        Creates a new WKBPolygon feature for each part of any WKBMultiPolygon 
        feature in the layer. This avoid relations with may 'outer' members in
        OSM data set. From this moment, localId will not be a unique identifier
        for buildings.
        """
        to_clean = []
        to_add = []
        for feature in self.getFeatures():
            geom = feature.geometry()
            if geom.wkbType() == QGis.WKBMultiPolygon:
                for part in geom.asMultiPolygon():
                    feat = QgsFeature(feature)
                    feat.setGeometry(QgsGeometry.fromPolygon(part))
                    to_add.append(feat)
                to_clean.append(feature.id())
        self.startEditing()
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            self.writer.addFeatures(to_add)
            log.debug(_("%d multi-polygons splited into %d polygons in "
                "the '%s' layer"), len(to_clean), len(to_add), 
                self.name().encode('utf-8'))
        self.commitChanges()

    def get_parents_per_vertex_and_features(self):
        """
        Returns:
            (dict) parent fids for each vertex, (dict) feature for each fid.
        """
        parents_per_vertex = defaultdict(list)
        features = {}
        for feature in self.getFeatures(): 
            features[feature.id()] = feature
            geom = feature.geometry()
            for ring in geom.asPolygon():
                for point in ring[0:-1]:
                    parents_per_vertex[point].append(feature.id())
        return (parents_per_vertex, features)
    
    def get_adjacents_and_features(self):
        """
        Returns:
            (list) groups of fids of adjacent polygons, (dict) feature for each fid.
        """
        (parents_per_vertex, features) = self.get_parents_per_vertex_and_features()
        adjs = []
        for (point, parents) in parents_per_vertex.items():
            if len(parents) > 1:
                for fid in parents:
                    geom = features[fid].geometry()
                    (point, ndx, ndxa, ndxb, dist) = geom.closestVertex(point)
                    next = geom.vertexAt(ndxb)
                    parents_next = parents_per_vertex[next]
                    common = set(x for x in parents if x in parents_next)
                    if len(common) > 1:
                        adjs.append(common)
        adjs = list(adjs)
        groups = []
        while adjs:
            group = set(adjs.pop())
            lastlen = -1
            while len(group) > lastlen:
                lastlen = len(group)
                for adj in adjs[:]:
                    if len({p for p in adj if p in group}) > 0:
                        group |= adj
                        adjs.remove(adj)
            groups.append(group)
        return (groups, features)
    
    def get_vertices(self):
        """Returns a in memory layer with the coordinates of each vertex"""
        vertices = QgsVectorLayer("Point", "vertices", "memory")
        to_add = []
        for feature in self.getFeatures(): 
            for ring in feature.geometry().asPolygon():
                for point in ring[0:-1]:
                    feat = QgsFeature(QgsFields())
                    geom = QgsGeometry.fromPoint(point)
                    feat.setGeometry(geom)
                    to_add.append(feat)
        vertices.startEditing() # layer with the coordinates of each vertex
        vertices.addFeatures(to_add)
        vertices.commitChanges()
        return vertices
    
    def get_duplicates(self, dup_thr=None):
        """
        Returns a dict of duplicated vertices for each coordinate.
        Two vertices are duplicated if they are nearest than dup_thr.
        """
        vertices = self.get_vertices()
        vertices_by_fid = {feat.id(): feat for feat in vertices.getFeatures()}
        index = QgsSpatialIndex(vertices.getFeatures())
        dup_thr = self.dup_thr if dup_thr is None else dup_thr
        duplicates = defaultdict(list)
        for vertex in vertices.getFeatures():
            point = Point(vertex.geometry().asPoint())
            area_of_candidates = point.boundingBox(dup_thr)
            fids = index.intersects(area_of_candidates)
            for fid in fids:
                dup = vertices_by_fid[fid].geometry().asPoint()
                dist = point.sqrDist(dup)
                if dup != point and dist < dup_thr**2:
                    duplicates[point].append(dup)
        return duplicates
        
    def merge_duplicates(self):
        """
        Reduces the number of distinct vertices in a polygon layer moving to the
        same position vertices nearest than 'dup_thr' meters.
        """
        dup_thr = self.dup_thr
        if log.getEffectiveLevel() <= logging.DEBUG:
            debshp = DebugWriter("debug_duplicated.shp", self.crs())
        (parents_per_vertex, features) = self.get_parents_per_vertex_and_features()
        dupes = 0
        duplicates = self.get_duplicates()
        duplist = sorted(duplicates.keys(), key=lambda x: -len(duplicates[x]))
        to_change = {}
        for point in duplist:
            for dup in duplicates[point]:
                for fid in parents_per_vertex[dup]:
                    feat = features[fid]
                    geom = feat.geometry()
                    (p, ndx, ndxa, ndxb, dist) = geom.closestVertex(dup)
                    if geom.moveVertex(point.x(), point.y(), ndx):
                        note = "refused by isGeosValid"
                        if geom.isGeosValid():
                            note = "Merge. %s" % feat['localId']
                            dupes += 1
                            to_change[fid] = geom
                        if log.getEffectiveLevel() <= logging.DEBUG:
                            debshp.add_point(p, note)
                if dup in duplist:
                    duplist.remove(dup)
        self.startEditing()
        if to_change:
            self.writer.changeGeometryValues(to_change)
            log.debug(_("Merged %d close vertices in the '%s' layer"), dupes, 
                self.name().encode('utf-8'))
        self.commitChanges()

    def clean_duplicated_nodes_in_polygons(self):
        """
        Cleans consecutives nodes with the same coordinates in any ring of a 
        polygon.
        """
        dupes = 0
        to_clean = []
        to_change = {}
        for feature in self.getFeatures(): 
            geom = feature.geometry()
            replace = False
            new_polygon = []
            for ring in geom.asPolygon():
                if ring:
                    merged = [ring[0]]
                    for i, point in enumerate(ring[1:]):
                        if point == ring[i]:
                            dupes += 1
                            replace=True
                        else:
                            merged.append(point)
                    new_polygon.append(merged)
            if replace:
                new_geom = QgsGeometry().fromPolygon(new_polygon)
                if new_geom and new_geom.isGeosValid():
                    to_change[feature.id()] = new_geom
                else:
                    to_clean.append(feature.id())
        self.startEditing()
        if to_change:
            self.writer.changeGeometryValues(to_change)
            log.debug(_("Merged %d duplicated vertices of polygons in "
                "the '%s' layer"), dupes, self.name().encode('utf-8'))
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            log.debug(_("Deleted %d invalid geometries in the '%s' layer"),
                len(to_clean), self.name().encode('utf-8'))
        self.commitChanges()

    def add_topological_points(self):
        """For each vertex in a polygon layer, adds it to nearest segments."""
        threshold = self.dist_thr # Distance threshold to create nodes
        straight_thr = self.straight_thr
        tp = 0
        if log.getEffectiveLevel() <= logging.DEBUG:
            debshp = DebugWriter("debug_topology.shp", self.crs())
        index = QgsSpatialIndex(self.getFeatures())
        features = {feat.id(): feat for feat in self.getFeatures()}

        to_change = {}
        for feature in features.values():
            geom = feature.geometry()
            for point in geom.asPolygon()[0][0:-1]: # excludes inner rings and last point:
                area_of_candidates = Point(point).boundingBox(threshold)
                for fid in index.intersects(area_of_candidates):
                    candidate = features[fid]
                    if fid != feature.id():
                        distance, closest, vertex = candidate.geometry() \
                                .closestSegmentWithContext(point)
                        g = QgsGeometry(candidate.geometry())
                        va = g.vertexAt(vertex)
                        vb = g.vertexAt(vertex - 1)
                        if distance < threshold**2 and point <> va and point <> vb:
                            note = "refused by angle"
                            angle = abs(point.azimuth(va) - point.azimuth(vb))
                            if abs(180 - angle) <= straight_thr:
                                note = "refused by insertVertex"
                                if g.insertVertex(point.x(), point.y(), vertex):
                                    note = "refused by isGeosValid"
                                    if g.isGeosValid():
                                        features[fid].setGeometry(g)
                                        note = "accepted"
                                        tp += 1
                                        to_change[fid] = g
                            if log.getEffectiveLevel() <= logging.DEBUG:
                                debshp.add_point(point, note)
        self.startEditing()
        if to_change:
            self.writer.changeGeometryValues(to_change)
            log.debug(_("Created %d topological points in the '%s' layer"), 
                tp, self.name().encode('utf-8'))
        self.commitChanges()
        if log.getEffectiveLevel() <= logging.DEBUG:
            del debshp

    def simplify(self):
        """
        Reduces the number of vertices in a polygon layer according to:

        * Delete vertex if the angle with its adjacents is below 'acute_thr'
        
        * Delete vertex if the angle with its adjacents is near of the straight 
          angle for less than 'straight_thr' degrees in all its parents.

        * Delete vertex if the distance to the segment formed by its parents is
          less than 'cath_thr' meters.

        * Delete invalid geometries
        """
        if log.getEffectiveLevel() <= logging.DEBUG:
            debshp = DebugWriter("debug_simplify.shp", self.crs())
        killed = 0
        to_change = {}
        to_clean = []
        # Clean acute vertices
        features = {feat.id(): feat for feat in self.getFeatures()}
        for fid, feat in features.items():
            geom = QgsGeometry(feat.geometry())
            n = -1
            while n < 0 or v != QgsPoint(0, 0):
                n += 1
                v = geom.vertexAt(n)
                (__, is_acute, __, __) = Point(v).get_angle_with_context(geom)
                if is_acute:
                    killed += 1
                    c = geom.centroid().asPoint()
                    geom.deleteVertex(n)
                    if geom.isGeosValid() and geom.area() > setup.min_area:
                        feat.setGeometry(geom)
                        to_change[fid] = geom
                        n = -1
                    else:
                        to_clean.append(fid)
                        if fid in to_change: del to_change[fid]
                        if log.getEffectiveLevel() <= logging.DEBUG:
                            debshp.add_point(c, "invalid geometry")
                        break
        self.startEditing()
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            log.debug(_("Deleted %d invalid geometries in the '%s' layer"), 
                len(to_clean), self.name().encode('utf-8'))
        self.commitChanges()
        # Clean non corners
        (parents_per_vertex, features) = self.get_parents_per_vertex_and_features()
        for pnt, parents in parents_per_vertex.items():
            # Test if this vertex is a 'corner' in any of its parent polygons
            point = Point(pnt)
            deb_values = []
            for fid in parents:
                feat = features[fid]
                geom = feat.geometry()
                (angle, is_acute, is_corner, cath) = point.get_angle_with_context(geom)
                deb_values.append((angle, is_acute, is_corner, cath))
                if is_corner: break
            msg = str(["angle=%.1f, is_acute=%s, is_corner=%s, cath=%.4f" % \
                    v for v in deb_values])
            if not is_corner:
                killed += 1      # delete the vertex from all its parents.
                for fid in frozenset(parents):
                    feat = features[fid]
                    geom = QgsGeometry(feat.geometry())
                    (__, ndx, __, __, __) = geom.closestVertex(point)
                    geom.deleteVertex(ndx)
                    if geom.isGeosValid():
                        feat.setGeometry(geom)
                        parents.remove(fid)
                        to_change[fid] = geom
                if log.getEffectiveLevel() <= logging.DEBUG:
                    debshp.add_point(point, "Deleted. %s" % msg)
            elif log.getEffectiveLevel() <= logging.DEBUG:
                debshp.add_point(point, "Keep. %s" % msg)
        self.startEditing()
        if to_change:
            self.writer.changeGeometryValues(to_change)
            log.debug(_("Simplified %d vertices in the '%s' layer"), killed, 
                self.name().encode('utf-8'))
        self.commitChanges()

    def merge_adjacents(self):
        """Merge polygons with shared segments"""
        (groups, features) = self.get_adjacents_and_features()
        self.startEditing()
        to_clean = []
        to_change = {}
        for group in groups:
            group = list(group)
            geom = features[group[0]].geometry()
            for fid in group[1:]:
                geom = geom.combine(features[fid].geometry())
            to_clean += group[1:]
            to_change[group[0]] = geom
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            self.writer.changeGeometryValues(to_change)
            log.debug(_("%d adjacent polygons merged into %d polygons in the '%s' "
                "layer"), len(to_clean), len(to_change), self.name().encode('utf-8'))
        self.commitChanges()

    def clean(self):
        """Merge duplicated vertices and simplify layer"""
        self.merge_duplicates()
        self.clean_duplicated_nodes_in_polygons()
        self.simplify()


class ParcelLayer(BaseLayer):
    """Class for cadastral parcels"""

    def __init__(self, path="Polygon", baseName="cadastralparcel", 
            providerLib="memory", source_date=None):
        super(ParcelLayer, self).__init__(path, baseName, providerLib)
        if self.pendingFields().isEmpty():
            self.dataProvider().addAttributes([
                    QgsField('localId', QVariant.String, len=254),
                QgsField('label', QVariant.String, len=254),
            ])
            self.updateFields()
        self.rename = {'localId': 'inspireId_localId'}
        self.source_date = source_date


class ZoningLayer(PolygonLayer):
    """Class for cadastral zoning"""

    def __init__(self, path="Polygon", baseName="cadastralzoning", 
            providerLib="memory", source_date=None):
        super(ZoningLayer, self).__init__(path, baseName, providerLib)
        if self.pendingFields().isEmpty():
            self.dataProvider().addAttributes([
                QgsField('localId', QVariant.String, len=254),
                QgsField('label', QVariant.String, len=254),
                QgsField('level', QVariant.String, len=254),
                QgsField('levelName', QVariant.String, len=254),
            ])
            self.updateFields()
        self.rename = {'localId': 'inspireId_localId'}
        self.source_date = source_date


class AddressLayer(BaseLayer):
    """Class for address"""

    def __init__(self, path="Point", baseName="address", providerLib="memory",
            source_date=None):
        super(AddressLayer, self).__init__(path, baseName, providerLib)
        if self.pendingFields().isEmpty():
            self.dataProvider().addAttributes([
                QgsField('localId', QVariant.String, len=254),
                QgsField('spec', QVariant.String, len=254),
                QgsField('designator', QVariant.String, len=254),
                QgsField('PD_id', QVariant.String, len=254),
                QgsField('TN_id', QVariant.String, len=254),
                QgsField('AU_id', QVariant.String, len=254)
            ])
            self.updateFields()
        self.rename = {'spec': 'specification'}
        self.resolve = {
            'PD_id': ('component_href', '[\w\.]+PD[\.0-9]+'), 
            'TN_id': ('component_href', '[\w\.]+TN[\.0-9]+'), 
            'AU_id': ('component_href', '[\w\.]+AU[\.0-9]+')
        }
        self.source_date = source_date

    def conflate(self, current_address):
        """
        Delete address existing in current_address
        
        Args:
            current_address (OSM): dataset
        """
        self.startEditing()
        to_clean = [feat.id() for feat in self.getFeatures() \
            if feat['TN_text'] + feat['designator'] in current_address]
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            log.debug(_("Refused %d addresses existing in OSM") % len(to_clean))
        to_clean = [feat.id() for feat in self.search("designator = '%s'" \
            % setup.no_number)]
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            log.debug(_("Deleted %d addresses without house number") % len(to_clean))
        self.commitChanges()

    def del_address(self, building_osm):
        """Delete the address if there aren't any associated building."""
        to_clean = []
        building_refs = (el.tags['ref'] for el in building_osm.elements \
            if 'ref' in el.tags)
        for ad in self.getFeatures():
            ref = ad['localId'].split('.')[-1]
            if ref in building_refs:
                to_clean.append(ad.id())
        if to_clean:
            self.startEditing()
            self.writer.deleteFeatures(to_clean)
            self.commitChanges()
            log.info(_("Deleted %d addresses"), len(to_clean))

    def get_highway_names(self, highway):
        """
        Returns a dictionary with the translation for each street name.
        
        Args:
            highway (HighwayLayer): Current OSM highway data
        
        Returns:
            (dict) highway names translations
        """
        index = QgsSpatialIndex(highway.getFeatures())
        features = {feat.id(): feat for feat in highway.getFeatures()}
        highway_names = {}
        for feat in self.getFeatures():
            name = feat['TN_text']
            query = self.search("TN_text='%s'" % name)
            points = [f.geometry().asPoint() for f in query]
            bbox = QgsGeometry().fromMultiPoint(points).boundingBox()
            choices = [features[fid]['name'] for fid in index.intersects(bbox)]
            highway_names[name] = hgwnames.match(name, choices)
        return highway_names


class ConsLayer(PolygonLayer):
    """Class for constructions"""

    def __init__(self, path="Polygon", baseName="building", 
            providerLib = "memory", source_date=None):
        super(ConsLayer, self).__init__(path, baseName, providerLib)
        if self.pendingFields().isEmpty():
            self.dataProvider().addAttributes([
                QgsField('localId', QVariant.String, len=254),
                QgsField('condition', QVariant.String, len=254),
                QgsField('link', QVariant.String, len=254),
                QgsField('currentUse', QVariant.String, len=254),
                QgsField('bu_units', QVariant.Int),
                QgsField('dwellings', QVariant.Int),
                QgsField('lev_above', QVariant.Int),
                QgsField('lev_below', QVariant.Int),
                QgsField('nature', QVariant.String, len=254),
                QgsField('task', QVariant.String, len=254),
                QgsField('fixme', QVariant.String, len=254)
            ])
            self.updateFields()
        self.rename = {
            'condition': 'conditionOfConstruction', 
            'link': 'documentLink' ,
            'bu_units': 'numberOfBuildingUnits', 
            'dwellings': 'numberOfDwellings',
            'lev_above': 'numberOfFloorsAboveGround',
            'lev_below': 'numberOfFloorsBelowGround',
            'nature': 'constructionNature'
        }
        self.source_date = source_date

    @staticmethod
    def is_building(feature):
        """Building features have not any underscore in its localId field"""
        return '_' not in feature['localId']

    @staticmethod
    def is_part(feature):
        """Part features have '_part' in its localId field"""
        return '_part' in feature['localId']
    
    @staticmethod
    def is_pool(feature):
        """Pool features have '_PI.' in its localId field"""
        return '_PI.' in feature['localId']

    def append_zone(self, layer, zone, processed):
        """Append features of layer inside zone excluding processed localId's'"""
        query = lambda f, kwargs: \
            f['localId'] not in kwargs['excluding'] and is_inside(f, kwargs['zone'])
        super(ConsLayer, self).append(layer, query=query, zone=zone, excluding=processed)

    def append_task(self, layer, task):
        """Append features of layer including task localId's'"""
        query = lambda f, kwargs: f['localId'].split('_')[0] in kwargs['including']
        super(ConsLayer, self).append(layer, query=query, including=task)

    def remove_parts_below_ground(self):
        """Remove all parts with 'lev_above' field equal 0."""
        self.startEditing()
        to_clean = [f.id() for f in self.search('lev_above=0')]
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            log.debug(_("Deleted %d building parts with no floors above ground"), 
                len(to_clean))
        self.commitChanges()

    def remove_outside_parts(self):
        """
        Remove parts outside the footprint of it building or without associated 
        building.
        Precondition: Called before merge_greatest_part
        """
        to_clean = []
        (buildings, parts) = self.index_of_building_and_parts()
        self.startEditing()
        for refcat in parts.keys():
            if refcat not in buildings:
                for part in parts[refcat]:
                    to_clean.append(part.id())
        for (refcat, bu) in buildings.items():
            if refcat in parts:
                for part in parts[refcat]:
                    if not is_inside(part, bu[0]):
                        to_clean.append(part.id())
        if to_clean:
            self.writer.deleteFeatures(to_clean)
            log.debug(_("Removed %d building parts outside the footprint"), len(to_clean))
        self.commitChanges()
            
    def merge_greatest_part(self, footprint, parts):
        """
        Given a building footprint and its parts:
        
        * Exclude parts not inside the footprint.

        * If the area of the parts above ground is equal to the area of the 
          footprint.

          * Sum the area for all the parts with the same level. Level is the 
            pair of values 'lev_above' and 'lev_below' (number of floors 
            above, and below groud).

          * For the level with greatest area, giving priority to parts with 
            rings to reduce relations, translate the number of floors 
            values to the footprint and deletes all the parts in that level.
        """
        parts_inside_footprint = [part for part in parts if is_inside(part, footprint)]
        area_for_level = defaultdict(list)
        levels_with_holes = []
        for part in parts_inside_footprint:
            level = (part['lev_above'], part['lev_below'])
            rings = part.geometry().asPolygon()
            area = part.geometry().area()
            if len(rings) > 1:
                levels_with_holes.append(level)
            if level[0] > 0: 
                area_for_level[level].append(area)
        to_clean = []
        to_change = {}
        if area_for_level:
            footprint_area = round(footprint.geometry().area()*100)
            parts_area = round(sum(sum(v) for v in area_for_level.values()) * 100)
            if footprint_area == parts_area:
                if levels_with_holes:
                    level_with_greatest_area = max(levels_with_holes, 
                        key=(lambda level: sum(area_for_level[level])))
                else:    
                    level_with_greatest_area = max(area_for_level.iterkeys(), 
                        key=(lambda level: sum(area_for_level[level])))
                for part in parts_inside_footprint:
                    if (part['lev_above'], part['lev_below']) == level_with_greatest_area:
                        to_clean.append(part.id())
                if to_clean:
                    attr = get_attributes(footprint)
                    attr[self.fieldNameIndex('lev_above')] = level_with_greatest_area[0]
                    attr[self.fieldNameIndex('lev_below')] = level_with_greatest_area[1]
                    to_change[footprint.id()] = attr 
        return to_clean, to_change

    def index_of_building_and_parts(self):
        """
        Constructs some utility dicts.
        buildings index building by localid (many if it was a multipart building).
        parts index parts of building by building localid.
        """
        buildings = defaultdict(list)
        parts = defaultdict(list)
        for feature in self.getFeatures():
            if self.is_building(feature):
                buildings[feature['localId']].append(feature)
            elif self.is_part(feature):
                localId = feature['localId'].split('_')[0]
                parts[localId].append(feature)
        return (buildings, parts)
    
    def merge_building_parts(self):
        """Apply merge_greatest_part to each set of building and its parts"""
        (buildings, parts) = self.index_of_building_and_parts()
        self.startEditing()
        to_clean = []
        to_change = {}
        for (refcat, group) in buildings.items():
            if refcat in parts:
                for building in group:
                    cn, ch = self.merge_greatest_part(building, parts[refcat])
                    to_clean += cn
                    to_change.update(ch)
        if to_clean:
            self.writer.changeAttributeValues(to_change)
            self.writer.deleteFeatures(to_clean)
            log.debug(_("Merged %d building parts to footprint"), len(to_clean))
        self.commitChanges()

    def remove_duplicated_holes(self):
        """
        Remove inner rings of parts and of buildings/pool if there exists another 
        feature with the same geometry
        """
        (parents_per_vertex, features) = self.get_parents_per_vertex_and_features()
        ip = 0
        to_change = {}
        self.startEditing()
        for feature in self.getFeatures():
            geom = QgsGeometry(feature.geometry())
            to_clean = []
            rings = geom.asPolygon()
            if ConsLayer.is_part(feature):
                if len(rings) > 1:
                    geom = QgsGeometry.fromPolygon([rings[0]])
                    ip += (len(rings) - 1)
                    to_change[feature.id()] = geom
            else:
                for (i, ring) in enumerate(rings[1:]):
                    first_parents = list(parents_per_vertex[ring[0]])
                    duplicated = all([parents_per_vertex[p] == first_parents \
                        for p in ring[1:-1]]) and len(first_parents) > 1
                    if duplicated:
                        to_clean.append(i + 1)
                        ip += 1
                if to_clean:
                    for ring in sorted(to_clean, reverse=True):
                        geom.deleteRing(ring)
                    to_change[feature.id()] = geom
        if ip:
            self.writer.changeGeometryValues(to_change)            
            log.debug(_("Removed %d duplicated inner rings"), ip)
        self.commitChanges()
                    
    def clean(self):
        """
        Merge duplicated vertices, add topological points, simplify layer
        and merge building parts.
        """
        self.merge_duplicates()
        self.clean_duplicated_nodes_in_polygons()
        self.add_topological_points()
        self.merge_building_parts()
        self.remove_duplicated_holes()
        self.simplify()

    def move_address(self, address, delete=True):
        """
        Move each address to the nearest point in the footprint of its 
        associated building (same cadastral reference), but only if:
        
        * There aren't more than one associated building.
        
        * The address specification is Entrance.
        
        * The new position is enough close and is not a corner

        If delete is True, remove the address if there aren't any associated building.
        """
        ad_count = 0
        to_clean = []
        to_change = {}
        to_move = {}
        to_insert = {}
        (buildings, parts) = self.index_of_building_and_parts()
        for ad in address.getFeatures():
            ad_count += 1
            attributes = get_attributes(ad)
            refcat = ad['localId'].split('.')[-1]
            building_count = len(buildings[refcat])
            if building_count == 0:
                if delete: to_clean.append(ad.id())
            elif building_count == 1:
                building = buildings[refcat][0]
                if ad['spec'] == 'Entrance':
                    point = ad.geometry().asPoint()
                    bg = building.geometry()
                    distance, closest, vertex = bg.closestSegmentWithContext(point)
                    va = bg.vertexAt(vertex - 1)
                    vb = bg.vertexAt(vertex)
                    if distance < setup.addr_thr**2:
                        if closest.sqrDist(va) < setup.entrance_thr**2 \
                                or closest.sqrDist(vb) < setup.entrance_thr**2:
                            attributes[ad.fieldNameIndex('spec')] = 'corner'
                            to_change[ad.id()] = attributes
                        else:
                            dg = QgsGeometry.fromPoint(closest)
                            to_move[ad.id()] = dg
                            bg.insertVertex(closest.x(), closest.y(), vertex)
                            to_insert[building.id()] = bg
                            for part in parts[refcat]:
                                pg = part.geometry()
                                for (i, vpa) in enumerate(pg.asPolygon()[0][0:-1]):
                                    vpb = pg.vertexAt(i+1)
                                    if va in (vpa, vpb) and vb in (vpa, vpb):
                                        pg.insertVertex(closest.x(), closest.y(), i+1)
                                        to_insert[part.id()] = pg
                    else:
                        attributes[ad.fieldNameIndex('spec')] = 'remote'
                        to_change[ad.id()] = attributes
            else:
                attributes[ad.fieldNameIndex('spec')] = 'relation'
                to_change[ad.id()] = attributes
        address.startEditing()
        if delete: address.writer.deleteFeatures(to_clean)
        address.writer.changeAttributeValues(to_change)
        address.writer.changeGeometryValues(to_move)
        address.commitChanges()
        self.startEditing()
        self.writer.changeGeometryValues(to_insert)
        self.commitChanges()
        log.debug(_("Deleted %d addresses, %d changed, %d moved"), len(to_clean), 
            len(to_change), len(to_move))

    def check_levels_and_area(self, min_level, max_level):
        """Shows distribution of floors and put fixmes to buildings too small or big"""
        to_change = {}
        field_ndx = self.pendingFields().fieldNameIndex('fixme')
        for feat in self.getFeatures():
            localid = feat['localId']
            if isinstance(feat['lev_above'], int) and feat['lev_above'] > 0:
                if localid not in max_level or feat['lev_above'] > max_level[localid]:
                    max_level[localid] = feat['lev_above']
            if isinstance(feat['lev_below'], int) and feat['lev_below'] > 0:
                if localid not in min_level or feat['lev_below'] > min_level[localid]:
                    min_level[localid] = feat['lev_below']
            if ConsLayer.is_building(feat):
                area = feat.geometry().area()
                attributes = get_attributes(feat)
                if area < setup.warning_min_area:
                    attributes[field_ndx] = _("Check, area too small")
                    to_change[feat.id()] = attributes
                if area > setup.warning_max_area:
                    attributes[field_ndx] = _("Check, area too big")
                    to_change[feat.id()] = attributes
        if to_change:
            self.startEditing()
            self.writer.changeAttributeValues(to_change)
            self.commitChanges()

    def conflate(self, current_bu_osm, delete=True):
        """
        Removes from current_bu_osm the buildings that don't have conflicts.
        If delete=False, only mark buildings with conflicts
        """
        index = QgsSpatialIndex(self.getFeatures())
        for el in frozenset(current_bu_osm.elements):
            poly = None
            if el.type == 'way' and 'building' in el.tags:
                poly = [[Point(p) for p in el.geometry()]]
            elif el.type == 'relation':
                poly = [[Point(p) for p in r] for r in el.geometry()]
            if poly is not None:
                geom = QgsGeometry().fromPolygon(poly)
                fids = index.intersects(geom.boundingBox())
                self.setSelectedFeatures(fids)
                conflict = False
                for feat in self.selectedFeatures():
                    if geom.contains(feat.geometry()) or \
                            geom.overlaps(feat.geometry()):
                        conflict = True
                        break    
                if delete and not conflict:
                    current_bu_osm.remove(el)
                elif conflict:
                    el.tags['conflict'] = 'yes'
                

class HighwayLayer(BaseLayer):
    """Class for OSM highways"""

    def __init__(self, path="LineString", baseName="highway", 
            providerLib="memory"):
        super(HighwayLayer, self).__init__(path, baseName, providerLib)
        if self.pendingFields().isEmpty():
            self.dataProvider().addAttributes([
                QgsField('name', QVariant.String, len=254),
            ])
            self.updateFields()
        self.setCrs(QgsCoordinateReferenceSystem(4326))

    def read_from_osm(self, data):
        """Get features from a osm dataset"""
        to_add = []
        for r in data.relations:
            for m in r.members:
                if m.type=='way':
                    m.element.tags['name'] = r.tags['name']
        for w in data.ways:
            points = [QgsPoint(n.x, n.y) for n in w.nodes]
            geom = QgsGeometry.fromPolyline(points)
            feat = QgsFeature(QgsFields(self.pendingFields()))
            feat.setGeometry(geom)
            feat.setAttribute("name", w.tags['name'])
            to_add.append(feat)
        self.startEditing()
        self.addFeatures(to_add)
        self.commitChanges()


class DebugWriter(QgsVectorFileWriter):
    """A QgsVectorFileWriter for debugging purposess."""

    def __init__(self, filename, crs, driver_name="ESRI Shapefile"):
        """
        Args:
            filename (str): File name of the layer
            crs (QgsCoordinateReferenceSystem): Crs of layer.
            driver_name (str): Defaults to ESRI Shapefile.
        """
        self.fields = QgsFields()
        self.fields.append(QgsField("note", QVariant.String, len=100))
        QgsVectorFileWriter.__init__(self, filename, "utf-8", self.fields, 
                QGis.WKBPoint, crs, driver_name)
    
    def add_point(self, point, note=None):
        """Adds a point to the layer with the attribute note."""
        feat = QgsFeature(QgsFields(self.fields))
        geom = QgsGeometry.fromPoint(point)
        feat.setGeometry(geom)
        if note:
            feat.setAttribute("note", note[:254])
        return self.addFeature(feat)

