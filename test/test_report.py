# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals
from builtins import str, bytes
import io
import mock
import unittest
import os
import locale
import random
import time
from collections import Counter
from datetime import datetime

os.environ['LANGUAGE'] = 'C'
import setup
import osm
import report


class TestReport(unittest.TestCase):

    def test_init(self):
        r = report.Report(foo = 'bar')
        self.assertEqual(r.foo, 'bar')

    def test_setattr(self):
        r = report.Report()
        r.mun_name = 'foobar'
        self.assertEqual(r.values['mun_name'], 'foobar')

    def test_getattr(self):
        r = report.Report()
        r.values['mun_name'] = 'foobar'
        self.assertEqual(r.mun_name, 'foobar')

    def test_get(self):
        r = report.Report()
        self.assertEqual(r.get('foo', 'bar'), 'bar')
        self.assertEqual(r.get('bar'), 0)

    def test_inc(self):
        r = report.Report()
        r.inc('foo')
        self.assertEqual(r.foo, 1)
        r.inc('foo', 2)
        self.assertEqual(r.foo, 3)

    def test_validate1(self):
        r = report.Report()
        r.inp_address_entrance = 6
        r.inp_address_parcel = 4
        r.inp_address = 10
        r.addresses_without_number = 1
        r.orphand_addresses = 2
        r.multiple_addresses = 1
        r.refused_addresses = 2
        r.out_address_entrance = 2
        r.out_address_building = 2
        r.out_addr_str = 3
        r.out_addr_plc = 1
        r.out_address = 4
        r.inp_features = 6
        r.inp_buildings = 2
        r.inp_parts = 3
        r.inp_pools = 1
        r.building_counter = {'a': 1, 'b': 2}
        r.out_buildings = 3
        r.out_features = 8
        r.orphand_parts = 1
        r.underground_parts = 1
        r.new_outlines = 2
        r.multipart_geoms_building = 2
        r.exploded_parts_building = 4
        r.validate()
        self.assertEqual(len(r.errors), 0)

    def test_validate2(self):
        r = report.Report()
        r.inp_address_entrance = 1
        r.inp_address_parcel = 2
        r.inp_address = 4
        r.addresses_without_number = 1
        r.orphand_addresses = 1
        r.multiple_addresses = 1
        r.refused_addresses = 1
        r.out_address_entrance = 1
        r.out_address_building = 2
        r.out_addr_str = 1
        r.out_addr_plc = 2
        r.out_address = 4
        r.inp_features = 7
        r.inp_buildings = 2
        r.inp_parts = 3
        r.inp_pools = 1
        r.building_counter = {'a': 1, 'b': 2}
        r.out_buildings = 4
        r.out_features = 8
        r.validate()
        msgs = [
            "Sum of address types should be equal to the input addresses",
            "Sum of output and deleted addresses should be equal to the input addresses",
            "Sum of entrance and building address should be equal to output addresses",
            "Sum of street and place addresses should be equal to output addresses",
            "Sum of buildings, parts and pools should be equal to the feature count",
            "Sum of building types should be equal to the number of buildings",
            "Sum of output and deleted minus created building features should be equal to input features"
        ]
        for msg in msgs:
            self.assertIn(msg, r.errors)

    def test_to_string0(self):
        r = report.Report()
        output = r.to_string()
        expected = "Date: " + datetime.now().strftime('%x') + setup.eol
        self.assertEqual(output, expected)

    def test_to_string1(self):
        r = report.Report()
        r.mun_name = 'Foobar'
        r.code = 99999
        r.inp_zip_codes = 1000
        r.fixmes = []
        output = r.to_string()
        expected = u"Municipality: Foobar" + setup.eol \
            + "Date: " + datetime.now().strftime('%x') + setup.eol + setup.eol \
            + "=Addresses=" + setup.eol + setup.eol \
            + "==Input data==" + setup.eol \
            + "Postal codes: " + report.int_format(1000) + setup.eol
        self.assertEqual(output, expected)

    def test_to_string2(self):
        r = report.Report()
        r.fixme_count = 2
        r.fixmes = ['f1', 'f2']
        r.warnings = ['w1', 'w2']
        output = r.to_string()
        expected = u"Date: " + datetime.now().strftime('%x') + setup.eol \
            + setup.eol + "=Problems=" + setup.eol \
            + "Fixmes: 2" + setup.eol \
            + report.TAB + "f1" + setup.eol + report.TAB + "f2" + setup.eol \
            + "Warnings: 2" + setup.eol \
            + report.TAB + "w1" + setup.eol + report.TAB + "w2" + setup.eol
        self.assertEqual(output, expected)

    def test_to_string3(self):
        r = report.Report(sys_info=True)
        output = r.to_string()
        expected = locale.format_string("Execution time: %.1f seconds", r.ex_time, 1)
        self.assertIn(expected, output)

    def test_to_file(self):
        r = report.Report()
        r.mun_name = "áéíóúñ"
        output = r.to_string()
        fn = 'test_report.txt'
        r.to_file(fn)
        with io.open(fn, 'r', encoding=setup.encoding) as fo:
            text = str(fo.read())
            text = text.replace('\n\n', setup.eol)
        self.assertEqual(output, text)
        if os.path.exists(fn):
            os.remove(fn)

    def test_address_stats(self):
        ad = osm.Osm()
        ad.Node(0,0, {'addr:street': 's1'})
        ad.Node(2,0, {'addr:street': 's2', 'entrance': 'yes'})
        ad.Node(4,0, {'addr:place': 'p1', 'entrance': 'yes'})
        ad.Way([], {'addr:street': 's3'})
        r = report.Report()
        r.address_stats(ad)
        self.assertEqual(r.out_addr_str, 3)
        self.assertEqual(r.out_addr_plc, 1)
        self.assertEqual(r.out_address_entrance, 2)
        self.assertEqual(r.out_address_building, 2)

    def test_cons_end_stats(self):
        r = report.Report()
        r.max_level = {'a': 1, 'b': 2, 'c': 2}
        r.min_level = {'a': 1, 'b': 1, 'c': 2}
        r.building_counter = {'a': 1, 'b': 2}
        r.cons_end_stats()
        self.assertEqual(set(r.dlag.split(', ')), set('1: 1, 2: 2'.split(', ')))
        self.assertEqual(set(r.dlbg.split(', ')), set('1: 2, 2: 1'.split(', ')))
        self.assertEqual(set(r.building_types.split(', ')), set('a: 1, b: 2'.split(', ')))

    def test_cons_stats(self):
        r = report.Report()
        r.building_counter = Counter()
        data = osm.Osm()
        data.Node(0,0, {'leisure': 'swimming_pool'})
        data.Node(0,0, {'building': 'a', 'fixme': 'f1'})
        data.Node(0,0, {'building': 'b', 'fixme': 'f2'})
        data.Node(0,0, {'building:part': 'yes', 'fixme': 'f2'})
        data.Node(0,0)
        r.cons_stats(data)
        self.assertEqual(r.out_pools, 1)
        self.assertEqual(r.out_buildings, 2)
        self.assertEqual(r.out_parts, 1)
        self.assertEqual(r.building_counter['a'], 1)
        self.assertEqual(r.building_counter['b'], 1)
        self.assertEqual(r.fixme_counter['f1'], 1)
        self.assertEqual(r.fixme_counter['f2'], 2)

    def test_fixme_stats(self):
        r = report.Report()
        r.fixme_counter = {}
        r.fixme_stats()
        self.assertEqual(r.fixme_stats(), 0)
        r.fixme_counter = {'a': 1, 'b': 2}
        r.fixme_stats()
        self.assertEqual(r.fixme_stats(), 3)
        self.assertEqual(len(r.fixmes), 2)
