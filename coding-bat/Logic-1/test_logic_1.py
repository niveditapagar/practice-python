import unittest
import cigar_party, date_fashion, squirrel_play, caught_speeding, sorta_sum, alarm_clock, love6, in1to10, near_ten


class MyTestCase(unittest.TestCase):
    def test_cigar_party(self):
        self.assertFalse(cigar_party.cigar_party(30, False))
        self.assertTrue(cigar_party.cigar_party(40, False))
        self.assertTrue(cigar_party.cigar_party(50, False))
        self.assertTrue(cigar_party.cigar_party(70, True))

    def test_date_fashion(self):
        self.assertEqual(date_fashion.date_fashion(5, 2), 0)
        self.assertEqual(date_fashion.date_fashion(5, 10), 2)
        self.assertEqual(date_fashion.date_fashion(5, 5), 1)
        self.assertEqual(date_fashion.date_fashion(10, 2), 0)

    def test_squirrel_play(self):
        self.assertTrue(squirrel_play.squirrel_play(70, False))
        self.assertTrue(squirrel_play.squirrel_play(95, True))
        self.assertFalse(squirrel_play.squirrel_play(95, False))
        self.assertFalse(squirrel_play.squirrel_play(59, True))
        self.assertTrue(squirrel_play.squirrel_play(90, False))

    def test_caught_speeding(self):
        self.assertEqual(caught_speeding.caught_speeding(60, False), 0)
        self.assertEqual(caught_speeding.caught_speeding(65, False), 1)
        self.assertEqual(caught_speeding.caught_speeding(65, True), 0)
        self.assertEqual(caught_speeding.caught_speeding(85, False), 2)
        self.assertEqual(caught_speeding.caught_speeding(90, True), 2)

    def test_sorta_sum(self):
        self.assertEqual(sorta_sum.sorta_sum(3, 4), 7)
        self.assertEqual(sorta_sum.sorta_sum(10, 9), 20)
        self.assertEqual(sorta_sum.sorta_sum(13, 4), 20)
        self.assertEqual(sorta_sum.sorta_sum(13, 14), 27)

    def test_alarm_clock(self):
        self.assertEqual(alarm_clock.alarm_clock(1, False), "7:00")
        self.assertEqual(alarm_clock.alarm_clock(5, False), "7:00")
        self.assertEqual(alarm_clock.alarm_clock(0, False), "10:00")
        self.assertEqual(alarm_clock.alarm_clock(0, True), "off")
        self.assertEqual(alarm_clock.alarm_clock(5, True), "10:00")

    def test_love6(self):
        self.assertTrue(love6.love6(6, 4))
        self.assertTrue(love6.love6(7, -1))
        self.assertFalse(love6.love6(4, 5))
        self.assertTrue(love6.love6(1, 5))
        self.assertTrue(love6.love6(16, 6))
        self.assertTrue(love6.love6(16, 10))

    def test_in1to10(self):
        self.assertTrue(in1to10.in1to10(5, False))
        self.assertTrue(in1to10.in1to10(11, True))
        self.assertFalse(in1to10.in1to10(6, True))
        self.assertFalse(in1to10.in1to10(11, False))
        self.assertFalse(in1to10.in1to10(-1, False))

    def test_near_ten(self):
        near_ten_numbers = [0, 1, 2, 8, 9, 10, 12, 19, 99, 1111, 220]
        not_near_ten_numbers = [5, 17, 23, 86]
        self.assertTrue(any(list(map(near_ten.near_ten, near_ten_numbers))))
        self.assertFalse(any(list(map(near_ten.near_ten, not_near_ten_numbers))))


if __name__ == '__main__':
    unittest.main()
