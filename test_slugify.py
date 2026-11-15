"""Tests for slugify."""
import unittest

from slugify import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_accents_stripped(self):
        self.assertEqual(slugify("Crème brûlée"), "creme-brulee")

    def test_multiple_spaces_collapsed(self):
        self.assertEqual(slugify("Hello   World"), "hello-world")

    def test_punctuation_removed(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_leading_trailing_trimmed(self):
        self.assertEqual(slugify("  Hello World  "), "hello-world")

    def test_custom_separator(self):
        self.assertEqual(slugify("Hello World", "_"), "hello_world")

    def test_non_string_raises(self):
        with self.assertRaises(TypeError):
            slugify(123)

    def test_empty_separator_raises(self):
        with self.assertRaises(ValueError):
            slugify("Hello", "")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_numbers_and_letters(self):
        self.assertEqual(slugify("Python 3.12"), "python-3-12")


if __name__ == "__main__":
    unittest.main()
