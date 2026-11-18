"""Tests for dedent_block."""
import unittest

from dedent_block import dedent_block


class DedentBlockTests(unittest.TestCase):
    def test_basic(self):
        text = "    Hello\n    World"
        result = dedent_block(text)
        expected = "Hello\nWorld"
        self.assertEqual(result, expected)

    def test_minimum_indent(self):
        text = "    Hello\n        World\n    Python"
        result = dedent_block(text)
        expected = "Hello\n    World\nPython"
        self.assertEqual(result, expected)

    def test_empty_lines_preserved(self):
        text = "    Hello\n\n    World"
        result = dedent_block(text)
        expected = "Hello\n\nWorld"
        self.assertEqual(result, expected)

    def test_blank_line_before_and_after(self):
        text = "\n    Hello\n    World\n"
        result = dedent_block(text)
        expected = "\nHello\nWorld\n"
        self.assertEqual(result, expected)

    def test_all_indented_by_more_than_zero(self):
        text = "      One\n      Two\n      Three"
        result = dedent_block(text)
        expected = "One\nTwo\nThree"
        self.assertEqual(result, expected)

    def test_no_indent(self):
        text = "Hello\nWorld"
        result = dedent_block(text)
        self.assertEqual(result, "Hello\nWorld")

    def test_single_line(self):
        text = "    Hello"
        result = dedent_block(text)
        self.assertEqual(result, "Hello")

    def test_empty_string(self):
        self.assertEqual(dedent_block(""), "")

    def test_whitespace_only_line_inside(self):
        text = "    Hello\n    \n    World"
        result = dedent_block(text)
        # The whitespace‑only line should remain as‑is.
        expected = "Hello\n    \nWorld"
        self.assertEqual(result, expected)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            dedent_block(123)

    def test_returns_new_string(self):
        original = "    Hello\n    World"
        result = dedent_block(original)
        # Ensure the original is not mutated.
        self.assertEqual(original, "    Hello\n    World")


if __name__ == "__main__":
    unittest.main()
