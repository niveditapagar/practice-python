import unittest
import double_char, count_hi, cat_dog, count_code, end_other, xyz_there


class MyTestCase(unittest.TestCase):
    def test_double_char(self):
        self.assertEqual(double_char.double_char('The'), 'TThhee')
        self.assertEqual(double_char.double_char('AAbb'), 'AAAAbbbb')
        self.assertEqual(double_char.double_char('Hi-There'), 'HHii--TThheerree')

    def test_count_hi(self):
        self.assertEqual(count_hi.count_hi('abc hi ho'), 1)
        self.assertEqual(count_hi.count_hi('ABChi hi'), 2)
        self.assertEqual(count_hi.count_hi('hihi'), 2)
        self.assertEqual(count_hi.count_hi('Hi is no HI on ahI'), 0)

    def test_cat_dog(self):
        self.assertTrue(cat_dog.cat_dog('abc hi ho'))
        self.assertTrue(cat_dog.cat_dog('catdog'))
        self.assertTrue(cat_dog.cat_dog('a cat is not a dog and a dog is not a cat'))
        self.assertTrue(cat_dog.cat_dog('abc'))
        self.assertTrue(cat_dog.cat_dog('a'))
        self.assertTrue(cat_dog.cat_dog(''))
        self.assertFalse(cat_dog.cat_dog('There are two cat cat but only one dog'))

    def test_count_code(self):
        self.assertEqual(count_code.count_code('abc hi ho'), 0)
        self.assertEqual(count_code.count_code('This is code'), 1)
        self.assertEqual(count_code.count_code('another cope'), 1)
        self.assertEqual(count_code.count_code('code cope cot'), 2)
        self.assertEqual(count_code.count_code('cod'), 0)
        self.assertEqual(count_code.count_code('co'), 0)
        self.assertEqual(count_code.count_code(''), 0)
        self.assertEqual(count_code.count_code('cone'), 1)

    def test_end_other(self):
        self.assertTrue(end_other.end_other('abc hi ho', 'ho'))
        self.assertFalse(end_other.end_other('abc hi ho', 'glow'))
        self.assertFalse(end_other.end_other('ab', 'ab12'))
        self.assertFalse(end_other.end_other('abcXYZ', 'abcDEF'))
        self.assertFalse(end_other.end_other('Hiabcx', 'bc'))
        self.assertTrue(end_other.end_other('Hiabc', 'bc'))

    def test_xyz_there(self):
        self.assertTrue(xyz_there.xyz_there("abcxyz"))
        self.assertFalse(xyz_there.xyz_there("abc.xyz"))
        self.assertTrue(xyz_there.xyz_there("xyz.abc"))
        self.assertTrue(xyz_there.xyz_there("abcxyz"))
        self.assertFalse(xyz_there.xyz_there("abc.xyz"))


if __name__ == '__main__':
    unittest.main()
