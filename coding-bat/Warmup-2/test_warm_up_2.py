import unittest
import string_times, front_times, string_bits, string_splosion, last2, array_count9, array_front9, array123, \
    string_match


class MyTestCase(unittest.TestCase):
    def test_string_times(self):
        self.assertEqual(string_times.string_times("Hi", 3), "HiHiHi")
        self.assertEqual(string_times.string_times("Hi", 2), "HiHi")
        self.assertEqual(string_times.string_times("Hi", 1), "Hi")
        self.assertEqual(string_times.string_times("Hi", 0), "")

    def test_front_times(self):
        self.assertEqual(front_times.front_times("Chocolate", 3), "ChoChoCho")
        self.assertEqual(front_times.front_times("Hi", 2), "HiHi")
        self.assertEqual(front_times.front_times("", 1), "")

    def test_string_bits(self):
        self.assertEqual(string_bits.string_bits("Chocolate"), "Cooae")
        self.assertEqual(string_bits.string_bits("Hi"), "H")
        self.assertEqual(string_bits.string_bits(""), "")

    def test_string_splosion(self):
        self.assertEqual(string_splosion.string_splosion("Code"), "CCoCodCode")
        self.assertEqual(string_splosion.string_splosion("abc"), "aababc")

    def test_last2(self):
        self.assertEqual(last2.last2("hixxhi"), 1)
        self.assertEqual(last2.last2("xaxxaxaxx"), 1)
        self.assertEqual(last2.last2("hi"), 0)
        self.assertEqual(last2.last2("axxxaaxx"), 2)

    def test_array_count9(self):
        self.assertEqual(array_count9.array_count9([1, 2, 9]), 1)
        self.assertEqual(array_count9.array_count9([1, 9, 9]), 2)
        self.assertEqual(array_count9.array_count9([1, 9, 9, 3, 9]), 3)
        self.assertEqual(array_count9.array_count9([]), 0)
        self.assertEqual(array_count9.array_count9([1, 2, 3]), 0)

    def test_array_front9(self):
        self.assertTrue(array_front9.array_front9([1, 2, 9, 3, 4]))
        self.assertFalse(array_front9.array_front9([1, 2, 3, 4, 9]))
        self.assertFalse(array_front9.array_front9([1, 2, 3, 4, 5]))
        self.assertFalse(array_front9.array_front9([]))
        self.assertTrue(array_front9.array_front9([9]))
        self.assertFalse(array_front9.array_front9([1, 2]))

    def test_array123(self):
        self.assertTrue(array123.array123([1, 1, 2, 3, 1]))
        self.assertFalse(array123.array123([1, 1, 2, 4, 1]))
        self.assertTrue(array123.array123([1, 1, 2, 1, 2, 3]))
        self.assertFalse(array123.array123([1, 1, 2, 1, 2, 1]))
        self.assertTrue(array123.array123([1, 2, 3, 1, 2, 3]))
        self.assertFalse(array123.array123([13]))

    def test_string_match(self):
        self.assertEqual(string_match.string_match('xxcaazz', 'xxbaaz'), 3)
        self.assertEqual(string_match.string_match('abc', 'abc'), 2)
        self.assertEqual(string_match.string_match('abc', 'axc'), 0)
        self.assertEqual(string_match.string_match('h', 'hello'), 0)
        self.assertEqual(string_match.string_match('', 'hello'), 0)


if __name__ == '__main__':
    unittest.main()
