import unittest
import sleep_in


class WarmUp1(unittest.TestCase):
    def test_sleep_in(self):
        self.assertEqual(sleep_in.sleep_in(True, True), True)
        self.assertEqual(sleep_in.sleep_in(False, False), True)
        self.assertEqual(sleep_in.sleep_in(True, False), False)
        self.assertEqual(sleep_in.sleep_in(False, True), True)


if __name__ == '__main__':
    unittest.main()
