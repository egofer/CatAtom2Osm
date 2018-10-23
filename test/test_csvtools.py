# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import str
import unittest
from tempfile import mkstemp

import csv
import io
import os
os.environ['LANGUAGE'] = 'C'

from csvtools import csv2dict, dict2csv
from setup import eol, encoding, delimiter


class TestCsvTools(unittest.TestCase):

    def test_csv2dict(self):
        _, tmp_path = mkstemp()
        with io.open(tmp_path, 'w', encoding=encoding) as csv_file:
            csv_file.write("á%sx%sé%sy%s" % (delimiter, eol, delimiter, eol))
        a_dict = csv2dict(tmp_path, {})
        self.assertEqual(a_dict, {"á":"x", "é":"y"})

    def test_csv2dict_bad_delimiter(self):
        _, tmp_path = mkstemp()
        with io.open(tmp_path, 'w', encoding=encoding) as csv_file:
            csv_file.write('a;1%sb;2' % eol)
        with self.assertRaises(IOError):
            a_dict = csv2dict(tmp_path, {})

    def test_dict2csv(self):
        _, tmp_path = mkstemp()
        d = {"á":'x', "é":'y'}
        l = list(d.items())
        t = "%s%s%s%s%s%s%s%s" % (l[0][0], delimiter, l[0][1], eol,
            l[1][0], delimiter, l[1][1], eol)
        dict2csv(tmp_path, d)
        with io.open(tmp_path, 'r', encoding=encoding) as csv_file:
            text = csv_file.read()
        self.assertEqual(text, t)

    def test_dict2csv_sort(self):
        _, tmp_path = mkstemp()
        dict2csv(tmp_path, {'b':'1', 'a':'3', 'c': '2'}, sort=1)
        with io.open(tmp_path, 'r', encoding=encoding) as csv_file:
            text = csv_file.read()
        self.assertEqual(text, "b%s1%sc%s2%sa%s3%s" % (delimiter, eol, 
            delimiter, eol, delimiter, eol))


