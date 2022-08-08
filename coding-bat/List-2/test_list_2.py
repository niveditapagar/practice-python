import unittest
import count_evens, big_diff, centered_average, sum13, sum67, has22


class MyTestCase(unittest.TestCase):
    def test_count_evens(self):
        self.assertEqual(count_evens.count_evens([2, 1, 2, 3, 4]), 3)
        self.assertEqual(count_evens.count_evens([2, 2, 0]), 3)
        self.assertEqual(count_evens.count_evens([1, 3, 5]), 0)
        self.assertEqual(count_evens.count_evens([]), 0)

    def test_big_diff(self):
        self.assertEqual(big_diff.big_diff([10, 3, 5, 6]), 7)
        self.assertEqual(big_diff.big_diff([7, 2, 10, 9]), 8)
        self.assertEqual(big_diff.big_diff([2]), 0)

    def test_centered_average(self):
        self.assertEqual(centered_average.centered_average([1, 2, 3, 4, 100]), 3)
        self.assertEqual(centered_average.centered_average([1, 1, 5, 5, 10, 8, 7]), 5)
        self.assertEqual(centered_average.centered_average([-10, -4, -2, -4, -2, 0]), -3)
        self.assertEqual(centered_average.centered_average([4, 4, 4, 4, 5]), 4)

    def test_sum13(self):
        self.assertEqual(sum13.sum13([1, 2, 2, 1]), 6)
        self.assertEqual(sum13.sum13([1, 1]), 2)
        self.assertEqual(sum13.sum13([1, 2, 2, 1, 13]), 6)
        self.assertEqual(sum13.sum13([1, 2, 2, 1, 13, 6, 6]), 12)
        self.assertEqual(sum13.sum13([13]), 0)
        self.assertEqual(sum13.sum13([13, 2]), 0)
        self.assertEqual(sum13.sum13([13, 2, 3]), 3)

    def test_sum67(self):
        self.assertEqual(sum67.sum67([1, 2, 2]), 5)
        self.assertEqual(sum67.sum67([1, 2, 2, 6, 99, 99, 7]), 5)
        self.assertEqual(sum67.sum67([1, 1, 6, 7, 2]), 4)
        self.assertEqual(sum67.sum67([1, 6, 7, 7]), 8)
        self.assertEqual(sum67.sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]), 2)

    def test_has22(self):
        self.assertTrue(has22.has22([1, 2, 2]))
        self.assertFalse(has22.has22([1, 2, 1, 2]))
        self.assertFalse(has22.has22([2, 1, 1]))
        self.assertTrue(has22.has22([2, 2]))
        self.assertFalse(has22.has22([2]))


if __name__ == '__main__':
    unittest.main()
