import unittest
import hello_name, make_abba, make_tags, make_out_word, extra_end, first_two, first_half, without_end, combo_string, \
    non_start


class MyTestCase(unittest.TestCase):
    def test_hello_name(self):
        self.assertEqual(hello_name.hello_name("Bob"), "Hello Bob!")
        self.assertEqual(hello_name.hello_name("Alice"), "Hello Alice!")
        self.assertEqual(hello_name.hello_name(""), "Hello !")

    def test_make_abba(self):
        self.assertEqual(make_abba.make_abba("Hi", "Bye"), "HiByeByeHi")
        self.assertEqual(make_abba.make_abba("Yo", "Alice"), "YoAliceAliceYo")
        self.assertEqual(make_abba.make_abba("What", "Up"), "WhatUpUpWhat")
        self.assertEqual(make_abba.make_abba("", "x"), "xx")
        self.assertEqual(make_abba.make_abba("x", ""), "xx")

    def test_make_tags(self):
        self.assertEqual(make_tags.make_tags("i", "Yay"), "<i>Yay</i>")
        self.assertEqual(make_tags.make_tags("i", "Hello"), "<i>Hello</i>")
        self.assertEqual(make_tags.make_tags("cite", "Hola"), "<cite>Hola</cite>")
        self.assertEqual(make_tags.make_tags("i", ""), "<i></i>")
        self.assertEqual(make_tags.make_tags("i", "i"), "<i>i</i>")

    def test_make_out_word(self):
        self.assertEqual(make_out_word.make_out_word("<<>>", "Yay"), "<<Yay>>")
        self.assertEqual(make_out_word.make_out_word("<<>>", "WooHooy"), "<<WooHooy>>")
        self.assertEqual(make_out_word.make_out_word("[[]]", "word"), "[[word]]")
        self.assertEqual(make_out_word.make_out_word("[[]]", ""), "[[]]")

    def test_extra_end(self):
        self.assertEqual(extra_end.extra_end("Hello"), "lololo")
        self.assertEqual(extra_end.extra_end("ab"), "ababab")
        self.assertEqual(make_out_word.make_out_word("[[]]", "word"), "[[word]]")
        self.assertEqual(make_out_word.make_out_word("[[]]", ""), "[[]]")

    def test_first_two(self):
        self.assertEqual(first_two.first_two("Hello"), "He")
        self.assertEqual(first_two.first_two("abcdefg"), "ab")
        self.assertEqual(first_two.first_two("xy"), "xy")
        self.assertEqual(first_two.first_two("x"), "x")
        self.assertEqual(first_two.first_two(""), "")

    def test_first_half(self):
        self.assertEqual(first_half.first_half("WooHoo"), "Woo")
        self.assertEqual(first_half.first_half("HelloThere"), "Hello")
        self.assertEqual(first_half.first_half("abcdef"), "abc")
        self.assertEqual(first_half.first_half("xy"), "x")
        self.assertEqual(first_half.first_half("a"), "")
        self.assertEqual(first_half.first_half(""), "")

    def test_without_end(self):
        self.assertEqual(without_end.without_end("WooHoo"), "ooHo")
        self.assertEqual(without_end.without_end("java"), "av")
        self.assertEqual(without_end.without_end("coding"), "odin")
        self.assertEqual(without_end.without_end("ab"), "")
        self.assertEqual(without_end.without_end("abc"), "b")
        self.assertEqual(without_end.without_end(""), "")

    def test_combo_string(self):
        self.assertEqual(combo_string.combo_string("Woo", "Hood"), "WooHoodWoo")
        self.assertEqual(combo_string.combo_string("Hello", "Hi"), "HiHelloHi")
        self.assertEqual(combo_string.combo_string("hi", "Hello"), "hiHellohi")
        self.assertEqual(combo_string.combo_string("aaa", "b"), "baaab")
        self.assertEqual(combo_string.combo_string("", ""), "")

    def test_non_start(self):
        self.assertEqual(non_start.non_start("Woo", "Hood"), "ooood")
        self.assertEqual(non_start.non_start("shotl", "java"), "hotlava")
        self.assertEqual(non_start.non_start("ab", "xy"), "by")
        self.assertEqual(non_start.non_start("ab", "x"), "b")
        self.assertEqual(non_start.non_start("a", "x"), "")


if __name__ == '__main__':
    unittest.main()
