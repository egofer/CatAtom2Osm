# -*- coding: utf-8 -*-
import unittest
import mock
import codecs
from cStringIO import StringIO
from contextlib import contextmanager
import random
import os, sys
os.environ['LANGUAGE'] = 'C'

import setup
import catatom

@contextmanager
def capture(command, *args, **kwargs):
    out = sys.stdout
    sys.stdout = codecs.getwriter('utf-8')(StringIO())
    try:
        command(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
    finally:
        sys.stdout = out

def raiseException():
    raise Exception

prov_atom = """<feed xmlns="http://www.w3.org/2005/Atom" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:georss="http://www.georss.org/georss"  xmlns:inspire_dls = "http://inspire.ec.europa.eu/schemas/inspire_dls/1.0" xml:lang="en"> 
<title>Download Office foobar</title>
<entry>
<title> 09001-FOO buildings</title>
</entry>
<entry>
<title> 09002-BAR buildings</title>
</entry>
<entry>
<title> 09003-TAZ buildings</title>
<georss:polygon>42.0997821981015 -3.79048777556759 42.0997821981015 -3.73420761211555 42.1181603073135 -3.73420761211555 42.1181603073135 -3.79048777556759 42.0997821981015 -3.79048777556759</georss:polygon>
</entry>
</feed>
"""

metadata = """<?xml version="1.0" encoding="ISO-8859-1"?>
<gmd:MD_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd" xmlns:gco="http://www.isotc211.org/2005/gco">
    <gmd:title>
        <gco:CharacterString>Buildings of 38001-TAZ (foo bar)</gco:CharacterString>
    </gmd:title>
	<gmd:dateStamp>
		<gco:Date>2017-02-25</gco:Date>
	</gmd:dateStamp>
    <gmd:code>
        <gco:CharacterString>http://www.opengis.net/def/crs/EPSG/0/32628</gco:CharacterString>
    </gmd:code>
    <gmd:EX_GeographicBoundingBox>
        <gmd:westBoundLongitude>
            <gco:Decimal>-16.7996857087189</gco:Decimal>
        </gmd:westBoundLongitude>
        <gmd:eastBoundLongitude>
            <gco:Decimal>-16.6878650661333</gco:Decimal>
        </gmd:eastBoundLongitude>
        <gmd:southBoundLatitude>
            <gco:Decimal>28.0655571972128</gco:Decimal>
        </gmd:southBoundLatitude>
        <gmd:northBoundLatitude>
            <gco:Decimal>28.1788414990302</gco:Decimal>
        </gmd:northBoundLatitude>
    </gmd:EX_GeographicBoundingBox>
</gmd:MD_Metadata>
"""

gmlfile = """<?xml version="1.0" encoding="ISO-8859-1"?>
<gml:FeatureCollection xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:AD="urn:x-inspire:specification:gmlas:Addresses:3.0">
    <AD:geometry>
        <gml:Point srsName="urn:ogc:def:crs:EPSG::32628"></gml:Point>
    </AD:geometry>
</gml:FeatureCollection>"""


class TestCatAtom(unittest.TestCase):

    def setUp(self):
        self.m_cat = mock.MagicMock()

    @mock.patch('catatom.os')
    def test_init(self, m_os):
        m_os.path.split = lambda x: x.split('/')
        self.m_cat.init = catatom.Reader.__init__.__func__
        with self.assertRaises(ValueError) as cm:
            self.m_cat.init(self.m_cat, '09999/xxxxx')
        self.assertIn('directory name', cm.exception.message)
        with self.assertRaises(ValueError) as cm:
            self.m_cat.init(self.m_cat, 'xxx/999')
        self.assertIn('directory name', cm.exception.message)
        with self.assertRaises(ValueError) as cm:
            self.m_cat.init(self.m_cat, 'xxx/99999')
        self.assertIn('Province code', cm.exception.message)
        m_os.path.exists.return_value = True
        m_os.path.isdir.return_value = False
        with self.assertRaises(IOError) as cm:
            self.m_cat.init(self.m_cat, 'xxx/12345')
        self.assertIn('Not a directory', cm.exception.message)
        m_os.makedirs.assert_not_called()
        m_os.path.exists.return_value = False
        m_os.path.isdir.return_value = True
        self.m_cat.init(self.m_cat, 'xxx/12345')
        m_os.makedirs.assert_called_with('xxx/12345')
        self.assertEquals(self.m_cat.path, 'xxx/12345')
        self.assertEquals(self.m_cat.zip_code, '12345')
        self.assertEquals(self.m_cat.prov_code, '12')

    @mock.patch('catatom.os')
    @mock.patch('catatom.open')
    def test_get_metadata_from_xml(self, m_open, m_os):
        self.m_cat.get_metadata = catatom.Reader.get_metadata.__func__
        m_os.path.exists.return_value = True
        m_open.return_value.read.return_value = metadata
        self.m_cat.get_metadata(self.m_cat, 'foo')
        m_open.assert_called_once_with('foo', 'r')
        self.assertEquals(self.m_cat.src_date, '2017-02-25')
        self.assertEquals(self.m_cat.cat_mun, 'TAZ')
        self.assertEquals(self.m_cat.crs_ref, 32628)

    @mock.patch('catatom.zipfile')
    def test_get_path_from_zip(self, m_zip):
        self.m_cat.get_path_from_zip = get_func(catatom.Reader.get_path_from_zip)
        a_path = os.path.join('foo', 'bar', 'taz')
        m_zip.namelist.return_value = ['xyz', '123taz', 'abc']
        full_path = self.m_cat.get_path_from_zip(self.m_cat, m_zip, a_path)
        self.assertEqual(full_path, '123taz')
        with self.assertRaises(KeyError) as ke:
            self.m_cat.get_path_from_zip(self.m_cat, m_zip, 'xxxxx')

    @mock.patch('catatom.os')
    @mock.patch('catatom.open')
    @mock.patch('catatom.zipfile')
    def test_get_metadata_from_zip(self, m_zip, m_open, m_os):
        self.m_cat.get_metadata = catatom.Reader.get_metadata.__func__
        m_os.path.exists.return_value = False
        m_zip.ZipFile.return_value.read.return_value = metadata
        self.m_cat.get_path_from_zip.return_value = 'foo'
        self.m_cat.get_metadata(self.m_cat, 'foo', 'bar')
<<<<<<< HEAD
        m_zip.ZipFile.assert_called_once_with('bar')
        m_os.path.basename.assert_called_once_with('foo')
        m_zip.ZipFile().read.assert_called_once_with(m_os.path.basename())
        self.assertEquals(self.m_cat.src_date, '2017-02-25')
        self.assertEquals(self.m_cat.cat_mun, 'TAZ')
        self.assertEquals(self.m_cat.crs_ref, 32628)
=======
        m_zip.ZipFile().read.assert_called_once_with('foo')
        self.assertEqual(self.m_cat.src_date, '2017-02-25')
        self.assertEqual(self.m_cat.cat_mun, 'TAZ')
        self.assertEqual(self.m_cat.crs_ref, 32628)
>>>>>>> dd7bd79... Fix problem resolving name of files in zips (issue #29)

    @mock.patch('catatom.os')
    @mock.patch('catatom.open')
    @mock.patch('catatom.etree')
    @mock.patch('catatom.hasattr')
    def test_get_metadata_empty(self, m_has, m_etree, m_open, m_os):
        self.m_cat.get_metadata = catatom.Reader.get_metadata.__func__
        m_os.path.exists.return_value = True
        del m_etree.fromstring.return_value.root
        m_etree.fromstring.return_value.__len__.return_value = 0
        m_has.return_value = False
        with self.assertRaises(IOError):
            self.m_cat.get_metadata(self.m_cat, 'foo')
        ns = m_etree.fromstring().find.call_args_list[0][0][1]
        self.assertEquals(set(ns.keys()), {'gco', 'gmd'})

    @mock.patch('catatom.os')
    @mock.patch('catatom.download')
    def test_get_atom_file(self, m_download, m_os):
        self.m_cat.get_atom_file = catatom.Reader.get_atom_file.__func__
        m_os.path.join = lambda *args: '/'.join(args)
        url = setup.prov_url['BU'].format(code='38')
        m_download.get_response.return_value.text = "xxxxhttpfobar/38001bartazzipxxx"
        self.m_cat.path = 'lorem'
        self.m_cat.zip_code = '38001'
        self.m_cat.get_atom_file(self.m_cat, url)
        m_download.wget.assert_called_once_with("httpfobar/38001bartazzip", "lorem/38001bartazzip")
        self.m_cat.zip_code = '38002'
        with self.assertRaises(ValueError):
            self.m_cat.get_atom_file(self.m_cat, url)

    @mock.patch('catatom.os')
    def test_get_layer_paths(self, m_os):
        self.m_cat.get_layer_paths = catatom.Reader.get_layer_paths.__func__
        m_os.path.join = lambda *args: '/'.join(args)
        with self.assertRaises(ValueError):
            self.m_cat.get_layer_paths(self.m_cat, 'foobar')
        self.m_cat.path = 'foo'
        self.m_cat.zip_code = 'bar'
        ln = random.choice(['building', 'buildingpart', 'otherconstruction'])
<<<<<<< HEAD
        (md_path, gml_path, zip_path, vsizip_path, g) = self.m_cat.get_layer_paths(self.m_cat, ln)
        self.assertEquals(g, 'BU')
        self.assertEquals(md_path, 'foo/A.ES.SDGC.BU.MD.bar.xml')
        self.assertEquals(gml_path, 'foo/A.ES.SDGC.BU.bar.' + ln + '.gml')
        self.assertEquals(zip_path, 'foo/A.ES.SDGC.BU.bar.zip')
        self.assertEquals(vsizip_path, '/vsizip/' + zip_path + '/' + gml_path.split('/')[-1])
        ln = random.choice(['cadastralparcel', 'cadastralzoning'])
        (md_path, gml_path, zip_path, vsizip_path, g) = self.m_cat.get_layer_paths(self.m_cat, ln)
        self.assertEquals(g, 'CP')
        self.assertEquals(md_path, 'foo/A.ES.SDGC.CP.MD..bar.xml')
        self.assertEquals(gml_path, 'foo/A.ES.SDGC.CP.bar.' + ln + '.gml')
        self.assertEquals(zip_path, 'foo/A.ES.SDGC.CP.bar.zip')
        ln = random.choice(['address', 'thoroughfarename', 'postaldescriptor', 'adminunitname'])
        (md_path, gml_path, zip_path, vsizip_path, g) = self.m_cat.get_layer_paths(self.m_cat, ln)
        self.assertEquals(g, 'AD')
        self.assertEquals(md_path, 'foo/A.ES.SDGC.AD.MD.bar.xml')
        self.assertEquals(gml_path, 'foo/A.ES.SDGC.AD.bar.gml|layername=' + ln)
        self.assertEquals(zip_path, 'foo/A.ES.SDGC.AD.bar.zip')
=======
        (md_path, gml_path, zip_path, g) = self.m_cat.get_layer_paths(self.m_cat, ln)
        self.assertEqual(g, 'BU')
        self.assertEqual(md_path, 'foo/A.ES.SDGC.BU.MD.bar.xml')
        self.assertEqual(gml_path, 'foo/A.ES.SDGC.BU.bar.' + ln + '.gml')
        self.assertEqual(zip_path, 'foo/A.ES.SDGC.BU.bar.zip')
        ln = random.choice(['cadastralparcel', 'cadastralzoning'])
        (md_path, gml_path, zip_path, g) = self.m_cat.get_layer_paths(self.m_cat, ln)
        self.assertEqual(g, 'CP')
        self.assertEqual(md_path, 'foo/A.ES.SDGC.CP.MD..bar.xml')
        self.assertEqual(gml_path, 'foo/A.ES.SDGC.CP.bar.' + ln + '.gml')
        self.assertEqual(zip_path, 'foo/A.ES.SDGC.CP.bar.zip')
        ln = random.choice(['address', 'thoroughfarename', 'postaldescriptor', 'adminunitname'])
        (md_path, gml_path, zip_path, g) = self.m_cat.get_layer_paths(self.m_cat, ln)
        self.assertEqual(g, 'AD')
        self.assertEqual(md_path, 'foo/A.ES.SDGC.AD.MD.bar.xml')
        self.assertEqual(gml_path, 'foo/A.ES.SDGC.AD.bar.gml')
        self.assertEqual(zip_path, 'foo/A.ES.SDGC.AD.bar.zip')
>>>>>>> dd7bd79... Fix problem resolving name of files in zips (issue #29)

    @mock.patch('catatom.os')
    @mock.patch('catatom.log')
    def test_download(self, m_log, m_os):
        self.m_cat.download = catatom.Reader.download.__func__
        g = random.choice(['BU', 'CP', 'AD'])
        url = setup.prov_url[g].format(code='99')
        self.m_cat.get_layer_paths.return_value = ('1', '2', '3', g)
        self.m_cat.prov_code = '99'
        self.m_cat.download(self.m_cat, 'foobar')
        self.m_cat.get_layer_paths.assert_called_once_with('foobar')
        self.m_cat.get_atom_file.assert_called_once_with(url)

    @mock.patch('catatom.os')
    @mock.patch('catatom.log')
    @mock.patch('catatom.layer')
    @mock.patch('catatom.QgsCoordinateReferenceSystem')
    def test_read(self, m_qgscrs, m_layer, m_log, m_os):
        self.m_cat.read = catatom.Reader.read.__func__
        g = random.choice(['BU', 'CP', 'AD'])
        self.m_cat.get_layer_paths.return_value = ('1', '2', '3', g)
        m_os.path.exists.return_value = True
        m_qgscrs.return_value.isValid.return_value = True
        self.m_cat.is_empty.return_value = False
        self.m_cat.crs_ref = '32628'
        self.m_cat.prov_code = '99'
        self.m_cat.src_date = 'bar'
        gml = self.m_cat.read(self.m_cat, 'foobar')
        self.m_cat.get_layer_paths.assert_called_once_with('foobar')
        self.m_cat.get_atom_file.assert_not_called()
        self.m_cat.get_metadata.assert_called_once_with('1', '3')
        self.m_cat.get_gml_from_zip.assert_called_once_with('2', '3', g, 'foobar')
        m_crs = m_qgscrs.return_value
        gml.setCrs.assert_called_once_with(m_crs)
        self.assertEquals(gml.source_date, 'bar')

        url = setup.prov_url[g].format(code='99')
        m_os.path.exists.return_value = False
        self.m_cat.is_empty.return_value = True
        gml = self.m_cat.read(self.m_cat, 'foobar', allow_empty=True)
        self.m_cat.get_atom_file.assert_called_once_with(url)
        output = m_log.info.call_args_list[-1][0][0]
        self.assertIn('empty', output)
<<<<<<< HEAD
        self.assertEquals(gml, None)
        m_layer.BaseLayer.assert_called_with('4', 'foobar.gml', 'ogr')
=======
        self.assertEqual(gml, None)
        self.m_cat.get_gml_from_zip.assert_called_once_with('2', '3', g, 'foobar')
>>>>>>> dd7bd79... Fix problem resolving name of files in zips (issue #29)

        m_os.path.exists.side_effect = [False, True]
        with self.assertRaises(IOError) as cm:
            self.m_cat.read(self.m_cat, 'foobar', force_zip=True)
        self.m_cat.get_atom_file.assert_called_with(url)
        self.assertIn('empty', cm.exception.message)

        m_layer.BaseLayer.return_value.crs.return_value.isValid.return_value = False
        m_qgscrs.return_value.isValid.return_value = False
        m_os.path.exists.side_effect = None
        self.m_cat.is_empty.return_value = False
        with self.assertRaises(IOError) as cm:
            self.m_cat.read(self.m_cat, 'foobar')
        self.assertIn('Could not determine the CRS', cm.exception.message)

        m_layer.BaseLayer.return_value.isValid.return_value = False
        self.m_cat.get_gml_from_zip.return_value = None
        with self.assertRaises(IOError) as cm:
            self.m_cat.read(self.m_cat, 'foobar')
        self.assertIn('Failed to load', cm.exception.message)

        self.m_cat.get_gml_from_zip.return_value = None
        m_layer.BaseLayer.return_value.isValid.return_value = True
        m_qgscrs.return_value.isValid.return_value = True
        gml = self.m_cat.read(self.m_cat, 'foobar')
        self.assertEquals(gml, m_layer.BaseLayer.return_value)

    def test_is_empty(self):
<<<<<<< HEAD
        test = catatom.Reader.is_empty.__func__(None, 'test/empty.gml|foo', 'test/empty.zip')
        self.assertTrue(test)
        test = catatom.Reader.is_empty.__func__(None, 'test/empty.gml', '')
        self.assertTrue(test)
        test = catatom.Reader.is_empty.__func__(None, 'test/building.gml', '')
=======
        self.m_cat.is_empty = get_func(catatom.Reader.is_empty)
        self.m_cat.get_path_from_zip.return_value = 'empty.gml'
        test = self.m_cat.is_empty(self.m_cat, 'test/empty.gml|foo', 'test/empty.zip')
        self.assertTrue(test)
        test = self.m_cat.is_empty(self.m_cat, 'test/empty.gml', '')
        self.assertTrue(test)
        test = self.m_cat.is_empty(self.m_cat, 'test/building.gml', '')
>>>>>>> dd7bd79... Fix problem resolving name of files in zips (issue #29)
        self.assertFalse(test)

    def test_get_path_from_zip(self):
        self.m_cat.get_path_from_zip = get_func(catatom.Reader.get_path_from_zip)
        zf = mock.MagicMock()
        zf.namelist.return_value = ['xxxfoo', 'yyybar']
        n = self.m_cat.get_path_from_zip(self.m_cat, zf, 'foo')
        self.assertEqual(n, 'xxxfoo')
        n = self.m_cat.get_path_from_zip(self.m_cat, zf, 'bar|xxx')
        self.assertEqual(n, 'yyybar')
        with self.assertRaises(KeyError) as cm:
            n = self.m_cat.get_path_from_zip(self.m_cat, zf, 'taz')
        self.assertIn('There is no item', str(cm.exception))

    @mock.patch('catatom.zipfile')
    @mock.patch('catatom.layer')
    def test_get_gml_from_zip(self, m_layer, m_zip):
        m_layer.BaseLayer.return_value.isValid.return_value = True
        zf = mock.MagicMock()
        m_zip.ZipFile.return_value = zf
        self.m_cat.get_path_from_zip.return_value = 'bar/gml_path'
        self.m_cat.get_gml_from_zip = get_func(catatom.Reader.get_gml_from_zip)
        gml = self.m_cat.get_gml_from_zip(self.m_cat, 'gml_path', 'foo\zip_path', 
            'group', 'ln')
        m_zip.ZipFile.assert_called_once_with('foo\zip_path')
        self.m_cat.get_path_from_zip.assert_called_once_with(zf, 'gml_path')
        self.assertEqual(gml, m_layer.BaseLayer.return_value)
        vsizip_path = '/vsizip/foo/zip_path/bar/gml_path'
        m_layer.BaseLayer.assert_called_once_with(vsizip_path, 'ln.gml', 'ogr')
        
    @mock.patch('catatom.zipfile')
    @mock.patch('catatom.layer')
    def test_get_gml_from_zip_ifs(self, m_layer, m_zip):
        m_layer.BaseLayer.return_value.isValid.return_value = False
        self.m_cat.get_path_from_zip.return_value = 'bar/gml_path'
        self.m_cat.get_gml_from_zip = get_func(catatom.Reader.get_gml_from_zip)
        gml = self.m_cat.get_gml_from_zip(self.m_cat, 'gml_path', 'foo\zip_path',
            'AD', 'ln')
        self.assertEqual(gml, None)
        vsizip_path = '/vsizip/foo/zip_path/bar/gml_path|layername=ln'
        m_layer.BaseLayer.assert_called_once_with(vsizip_path, 'ln.gml', 'ogr')

    @mock.patch('catatom.log.warning')
    @mock.patch('catatom.overpass')
    @mock.patch('catatom.hgwnames')
    @mock.patch('catatom.download')
    def test_get_boundary(self, m_download, m_hgw, m_overpass, m_log):
        self.m_cat.get_boundary = catatom.Reader.get_boundary.__func__
        zoning = mock.MagicMock()
        bbox = "28.0655571972128,-16.7996857087189,28.1788414990302,-16.6878650661333"
        zoning.bounding_box.return_value = bbox
        data = {"id": 2, "tags": {"name": "Tazmania"}}
        m_hgw.fuzz = True
        m_hgw.dsmatch.return_value = data
        m_overpass.Query.return_value.read.return_value = '{"elements": "foobar"}'
        self.m_cat.prov_code = '09'
        self.m_cat.zip_code = '09003'
        self.m_cat.cat_mun = 'TAZ'
        self.m_cat.get_boundary(self.m_cat, zoning)
        m_overpass.Query.assert_called_with(bbox, 'json', False, False)
        self.assertEquals(m_hgw.dsmatch.call_args_list[0][0][0], 'TAZ')
        self.assertEquals(m_hgw.dsmatch.call_args_list[0][0][1], 'foobar')
        self.assertEquals(m_hgw.dsmatch.call_args_list[0][0][2](data), 'Tazmania')
        self.assertEquals(self.m_cat.boundary_search_area, '2')
        self.assertEquals(self.m_cat.boundary_name, 'Tazmania')
        
        m_hgw.dsmatch.return_value = None
        self.m_cat.get_boundary(self.m_cat, zoning)
        output = m_log.call_args_list[0][0][0]
        self.assertIn("Failed to find", output)
        self.assertEquals(self.m_cat.boundary_search_area, bbox)
        
        m_overpass.Query.return_value.read = raiseException
        self.m_cat.get_boundary(self.m_cat, zoning)
        output = m_log.call_args_list[1][0][0]
        self.assertIn("Failed to find", output)
        
        m_hgw.fuzz = False
        self.m_cat.zip_code = '07032'
        self.m_cat.get_boundary(self.m_cat, zoning)
        self.assertEquals(self.m_cat.boundary_name, u'Maó')

    @mock.patch('catatom.download')
    def test_list_municipalities(self, m_download):
        with self.assertRaises(ValueError):
            catatom.list_municipalities('01')
        url = setup.prov_url['BU'].format(code='09')
        m_download.get_response.return_value.content = prov_atom
        with capture(catatom.list_municipalities, '09') as output:
            m_download.get_response.assert_called_once_with(url)
            self.assertIn('foobar', output)
            self.assertIn('FOO', output)
            self.assertIn('BAR', output)

