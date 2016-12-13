from phedex import _cleanDictionary
from units import fmtscaled

import unittest

class TestPhedex(unittest.TestCase):
    def testCleanDict(self):
        dictionary = {'a':1, 'b':3, 'c':4, 'd':5}
        retain = ['a', 'd']
        cleaned_dict = _cleanDictionary(dictionary, retain)
        self.assertTrue(cleaned_dict.has_key('a'))
        self.assertTrue(cleaned_dict.has_key('d'))
        self.assertFalse(cleaned_dict.has_key('b'))
        self.assertFalse(cleaned_dict.has_key('c'))

    def testUnitFormatting(self):
        number = 10**6
        number = fmtscaled(number, unit='B')
        self.assertEqual(number, '1.0 MB')
        number = 10**12
        number = fmtscaled(number, unit='B')
        self.assertEqual(number, '1.0 TB')

if __name__ == '__main__':
    unittest.main()
