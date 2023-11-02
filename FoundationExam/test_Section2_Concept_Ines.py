# 2.2 - I have created comprehensive unit tests with valid, invalid and boundary tests

import unittest
from Section2_Concept_Ines import is_isogram, InvalidInput

class TestIsIsogram(unittest.TestCase):
    def test_isIsogram_valid_ines(self):
        self.assertEqual(True, is_isogram("ines"))

    def test_isIsogram_valid_ana(self):
        self.assertEqual(False, is_isogram("ana"))

    def test_isIsogram_valid_isogram(self):
        self.assertEqual(True, is_isogram("isogram"))

    def test_isIsogram_valid_boundary_Ana(self):
        self.assertEqual(False, is_isogram("Ana"))

    def test_divide_invalid_boundary_invalidinput(self):
        with self.assertRaises(InvalidInput):
            is_isogram(6)


if __name__ == '__main__':
    unittest.main()