import unittest

import sleep_in, monkey_trouble, sum_double, diff21, parrot_trouble, makes10, near_hundred, pos_neg, not_string, \
    missing_char, front_back, front3


class WarmUp1(unittest.TestCase):
    def test_sleep_in(self):
        self.assertTrue(sleep_in.sleep_in(True, True))
        self.assertTrue(sleep_in.sleep_in(False, False))
        self.assertFalse(sleep_in.sleep_in(True, False))
        self.assertTrue(sleep_in.sleep_in(False, True))

    def test_monkey_trouble(self):
        self.assertTrue(monkey_trouble.monkey_trouble(True, True))
        self.assertTrue(monkey_trouble.monkey_trouble(False, False))
        self.assertFalse(monkey_trouble.monkey_trouble(False, True))
        self.assertFalse(monkey_trouble.monkey_trouble(True, False))

    def test_sum_double(self):
        self.assertEqual(sum_double.sum_double(1, 2), 3)
        self.assertEqual(sum_double.sum_double(-1, 0), -1)
        self.assertEqual(sum_double.sum_double(2, 2), 8)
        self.assertEqual(sum_double.sum_double(0, 0), 0)

    def test_diff21(self):
        self.assertEqual(diff21.diff21(19), 2)
        self.assertEqual(diff21.diff21(21), 0)
        self.assertEqual(diff21.diff21(29), 16)
        self.assertEqual(diff21.diff21(0), 21)
        self.assertEqual(diff21.diff21(-1), 22)

    def test_parrot_trouble(self):
        self.assertTrue(parrot_trouble.parrot_trouble(True, 6))
        self.assertFalse(parrot_trouble.parrot_trouble(True, 7))
        self.assertFalse(parrot_trouble.parrot_trouble(False, 6))
        self.assertTrue(parrot_trouble.parrot_trouble(True, 21))
        self.assertFalse(parrot_trouble.parrot_trouble(False, 12))

    def test_makes10(self):
        test_numbers_makes_10_a = [9, 1, 10, 10, -2, 5]
        test_numbers_makes_10_b = [10, 9, 80, 10, 12, 5]
        self.assertTrue(all(list(map(makes10.makes10, test_numbers_makes_10_a, test_numbers_makes_10_b))))
        self.assertFalse(makes10.makes10(2, 2))

    def test_near_hundred(self):
        test_numbers_near_hundred = [93, 90, 110, 203, 198]
        self.assertTrue(all(list(map(near_hundred.near_hundred, test_numbers_near_hundred))))

        test_numbers_not_near_hundred = [89, 0, -1, 212, 119, 180]
        self.assertFalse(all(list(map(near_hundred.near_hundred, test_numbers_not_near_hundred))))

    def test_pos_neg(self):
        self.assertTrue(pos_neg.pos_neg(1, -1, False))
        self.assertTrue(pos_neg.pos_neg(-1, 1, False))
        self.assertTrue(pos_neg.pos_neg(-4, -5, True))
        self.assertFalse(pos_neg.pos_neg(-24, -15, False))
        self.assertFalse(pos_neg.pos_neg(-24, 15, True))
        self.assertFalse(pos_neg.pos_neg(224, 115, True))
        self.assertFalse(pos_neg.pos_neg(324, 1500, False))

    def test_not_string(self):
        self.assertEqual(not_string.not_string("candy"), "not candy")
        self.assertEqual(not_string.not_string("x"), "not x")
        self.assertEqual(not_string.not_string("not bad"), "not bad")
        self.assertEqual(not_string.not_string("bad"), "not bad")
        self.assertEqual(not_string.not_string("not"), "not")

    def test_missing_char(self):
        self.assertEqual(missing_char.missing_char("kitten", 1), "ktten")
        self.assertEqual(missing_char.missing_char("kitten", 0), "itten")
        self.assertEqual(missing_char.missing_char("kitten", 5), "kitte")

    def test_front_back(self):
        self.assertEqual(front_back.front_back("code"), "eodc")
        self.assertEqual(front_back.front_back(""), "")
        self.assertEqual(front_back.front_back("a"), "a")
        self.assertEqual(front_back.front_back("so"), "os")
        self.assertEqual(front_back.front_back("chocolate"), "ehocolatc")

    def test_front3(self):
        self.assertEqual(front3.front3(""), "")
        self.assertEqual(front3.front3("a"), "aaa")
        self.assertEqual(front3.front3("so"), "sososo")
        self.assertEqual(front3.front3("cat"), "catcatcat")
        self.assertEqual(front3.front3("chocolate"), "chochocho")


if __name__ == '__main__':
    unittest.main()
