from __future__ import unicode_literals
import unittest
import mock
import locale
import os, sys  
os.environ['LANGUAGE'] = 'C'

import setup

class TestSetup(unittest.TestCase):

    def test_win(self):
        eol = setup.eol
        lang = os.getenv('LANG')
        setup.platform = 'linux2'
        setup.winenv()
        self.assertEqual(setup.eol, '\n')
        setup.platform = 'winx'
        setup.winenv()
        self.assertEqual(setup.eol, '\r\n')
        setup.language = 'foobar'
        del os.environ['LANG']
        setup.winenv()
        self.assertEqual(os.getenv('LANG'), 'foobar')
        os.environ['LANG'] = lang
        setup.eol = eol

