import unittest
import make_bricks, lone_sum, lucky_sum, no_teen_sum, round_sum, close_far, make_chocolate


class MyTestCase(unittest.TestCase):
    def test_make_bricks(self):
        self.assertTrue(make_bricks.make_bricks(3, 1, 8))
        self.assertFalse(make_bricks.make_bricks(3, 1, 9))
        self.assertTrue(make_bricks.make_bricks(3, 2, 10))
        self.assertFalse(make_bricks.make_bricks(3, 2, 9))

    def test_lone_sum(self):
        self.assertEqual(lone_sum.lone_sum(1, 2, 3), 6)
        self.assertEqual(lone_sum.lone_sum(3, 2, 3), 2)
        self.assertEqual(lone_sum.lone_sum(3, 3, 3), 0)
        self.assertEqual(lone_sum.lone_sum(2, 9, 3), 14)

    def test_lucky_sum(self):
        self.assertEqual(lucky_sum.lucky_sum(1, 2, 3), 6)
        self.assertEqual(lucky_sum.lucky_sum(1, 2, 13), 3)
        self.assertEqual(lucky_sum.lucky_sum(1, 13, 3), 1)
        self.assertEqual(lucky_sum.lucky_sum(13, 2, 3), 0)

    def test_no_teen_sum(self):
        self.assertEqual(no_teen_sum.no_teen_sum(1, 2, 3), 6)
        self.assertEqual(no_teen_sum.no_teen_sum(2, 13, 1), 3)
        self.assertEqual(no_teen_sum.no_teen_sum(2, 1, 14), 3)
        self.assertEqual(no_teen_sum.no_teen_sum(16, 17, 14), 16)
        self.assertEqual(no_teen_sum.no_teen_sum(16, 15, 2), 33)

    def test_round_sum(self):
        self.assertEqual(round_sum.round_sum(16, 17, 18), 60)
        self.assertEqual(round_sum.round_sum(12, 13, 14), 30)
        self.assertEqual(round_sum.round_sum(6, 4, 4), 10)
        self.assertEqual(round_sum.round_sum(25, 24, 25), 80)
        self.assertEqual(round_sum.round_sum(12, 10, 24), 40)

    def test_close_far(self):
        self.assertTrue(close_far.close_far(1, 2, 10))
        self.assertTrue(close_far.close_far(4, 1, 3))
        self.assertTrue(close_far.close_far(8, 6, 9))
        self.assertFalse(close_far.close_far(1, 2, 3))
        self.assertFalse(close_far.close_far(4, 5, 3))
        self.assertFalse(close_far.close_far(8, 9, 7))

    def test_make_chocolate(self):
        self.assertEqual(make_chocolate.make_chocolate(4, 1, 9), 4)
        self.assertEqual(make_chocolate.make_chocolate(4, 1, 10), -1)
        self.assertEqual(make_chocolate.make_chocolate(4, 1, 7), 2)
        self.assertEqual(make_chocolate.make_chocolate(6, 1, 10), 5)
        self.assertEqual(make_chocolate.make_chocolate(7, 1, 13), -1)
        self.assertEqual(make_chocolate.make_chocolate(60, 100, 550), 50)
        self.assertEqual(make_chocolate.make_chocolate(40, 100, 550), -1)
        self.assertEqual(make_chocolate.make_chocolate(55, 99, 550), 55)
        self.assertEqual(make_chocolate.make_chocolate(45, 120, 550), 0)
        self.assertEqual(make_chocolate.make_chocolate(125, 90, 550), 100)


if __name__ == '__main__':
    unittest.main()
