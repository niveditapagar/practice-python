import unittest
import first_last6, same_first_last, make_pi, common_end, sum3, rotate_left3, reverse3, max_end3, sum2, middle_way, \
    make_ends, has23


class MyTestCase(unittest.TestCase):
    def test_first_last6(self):
        self.assertTrue(first_last6.first_last6([1, 2, 6]))
        self.assertTrue(first_last6.first_last6([6, 9, 3, 1, 2, 6]))
        self.assertTrue(first_last6.first_last6([6]))
        self.assertTrue(first_last6.first_last6([1, 6]))
        self.assertFalse(first_last6.first_last6([1, 2, 3, 4, 5]))
        self.assertFalse(first_last6.first_last6([1, 2, 6, 4, 5]))
        self.assertFalse(first_last6.first_last6([1]))

    def test_same_first_last(self):
        self.assertTrue(same_first_last.same_first_last([1, 2, 3, 1]))
        self.assertTrue(same_first_last.same_first_last([1, 2, 1]))
        self.assertTrue(same_first_last.same_first_last([7]))
        self.assertTrue(same_first_last.same_first_last([8, 8]))
        self.assertFalse(same_first_last.same_first_last([1, 2, 3]))
        self.assertFalse(same_first_last.same_first_last([]))
        self.assertFalse(same_first_last.same_first_last([10, 9]))

    def test_make_pi(self):
        self.assertEqual(make_pi.make_pi(), [3, 1, 4])

    def test_common_end(self):
        self.assertTrue(common_end.common_end([1, 2, 3], [7, 3]))
        self.assertFalse(common_end.common_end([1, 2, 3], [7, 3, 2]))
        self.assertTrue(common_end.common_end([1, 2, 3], [1, 3]))
        self.assertTrue(common_end.common_end([1, 2, 3], [1]))
        self.assertFalse(common_end.common_end([1, 2, 3], [2]))

    def test_sum3(self):
        self.assertEqual(sum3.sum3([1, 2, 3]), 6)
        self.assertEqual(sum3.sum3([5, 11, 2]), 18)
        self.assertEqual(sum3.sum3([7, 0, 0]), 7)

    def test_rotate_left3(self):
        self.assertEqual(rotate_left3.rotate_left3([1, 2, 3]), [2, 3, 1])
        self.assertEqual(rotate_left3.rotate_left3([0, 0, 7]), [0, 7, 0])

    def test_reverse3(self):
        self.assertEqual(reverse3.reverse3([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse3.reverse3([5, 11, 9]), [9, 11, 5])

    def test_max_end3(self):
        self.assertEqual(max_end3.max_end3([1, 2, 3]), [3, 3, 3])
        self.assertEqual(max_end3.max_end3([6, 2, 3]), [6, 6, 6])
        self.assertEqual(max_end3.max_end3([6, 2, 6]), [6, 6, 6])

    def test_sum2(self):
        self.assertEqual(sum2.sum2([1, 2, 3]), 3)
        self.assertEqual(sum2.sum2([1, 1]), 2)
        self.assertEqual(sum2.sum2([1, 1, 1]), 2)
        self.assertEqual(sum2.sum2([10]), 10)
        self.assertEqual(sum2.sum2([]), 0)

    def test_middle_way(self):
        self.assertEqual(middle_way.middle_way([1, 2, 3], [4, 5, 6]), [2, 5])
        self.assertEqual(middle_way.middle_way([7, 7, 7], [3, 8, 0]), [7, 8])
        self.assertEqual(middle_way.middle_way([5, 2, 9], [1, 4, 5]), [2, 4])

    def test_make_ends(self):
        self.assertEqual(make_ends.make_ends([1, 2, 3]), [1, 3])
        self.assertEqual(make_ends.make_ends([7, 8]), [7, 8])
        self.assertEqual(make_ends.make_ends([1]), [1, 1])
        self.assertEqual(make_ends.make_ends([7, 8, 9, 7]), [7, 7])

    def test_has23(self):
        self.assertTrue(has23.has23([1, 2]))
        self.assertTrue(has23.has23([3, 2]))
        self.assertTrue(has23.has23([3, 10]))
        self.assertFalse(has23.has23([1, 11]))


if __name__ == '__main__':
    unittest.main()
