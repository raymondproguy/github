"""Tests for word_wrap."""
import unittest

from word_wrap import word_wrap


class WordWrapTests(unittest.TestCase):
    def test_basic(self):
        text = "Hello World Python"
        result = word_wrap(text, 10)
        expected = "Hello\nWorld\nPython"
        self.assertEqual(result, expected)

    def test_multiple_spaces(self):
        text = "Hello   World"
        result = word_wrap(text, 10)
        self.assertEqual(result, "Hello\nWorld")

    def test_long_word_split(self):
        text = "supercalifragilistic"
        result = word_wrap(text, 5)
        self.assertEqual(result, "super\ncalif\nragil\nistic")

    def test_exact_width(self):
        text = "ab cd"
        result = word_wrap(text, 2)
        self.assertEqual(result, "ab\ncd")

    def test_width_one(self):
        text = "a b"
        result = word_wrap(text, 1)
        self.assertEqual(result, "a\nb")

    def test_newlines_preserved(self):
        text = "Hello World\nThis is a test"
        result = word_wrap(text, 8)
        expected = "Hello\nWorld\nThis is\na test"
        self.assertEqual(result, expected)

    def test_empty_string(self):
        self.assertEqual(word_wrap("", 10), "")

    def test_width_validation(self):
        with self.assertRaises(ValueError):
            word_wrap("Hello", 0)
        with self.assertRaises(ValueError):
            word_wrap("Hello", -1)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            word_wrap(123, 10)
        with self.assertRaises(TypeError):
            word_wrap("Hello", 10.5)

    def test_width_larger_than_text(self):
        text = "short"
        result = word_wrap(text, 100)
        self.assertEqual(result, "short")


if __name__ == "__main__":
    unittest.main()
