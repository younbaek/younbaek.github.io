#!/usr/bin/env python3
"""Test for saving text files."""

import os
import tempfile
import unittest


class TextFileSaveTest(unittest.TestCase):
    """Test cases for saving text files."""

    def setUp(self):
        """Create a temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up temporary files."""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_save_simple_text_file(self):
        """Test saving a simple text file."""
        test_file = os.path.join(self.test_dir, "test.txt")
        content = "Hello, World!"

        with open(test_file, "w") as f:
            f.write(content)

        self.assertTrue(os.path.exists(test_file))
        with open(test_file, "r") as f:
            saved_content = f.read()
        self.assertEqual(saved_content, content)

    def test_save_multiline_text_file(self):
        """Test saving a multiline text file."""
        test_file = os.path.join(self.test_dir, "multiline.txt")
        content = "Line 1\nLine 2\nLine 3"

        with open(test_file, "w") as f:
            f.write(content)

        self.assertTrue(os.path.exists(test_file))
        with open(test_file, "r") as f:
            saved_content = f.read()
        self.assertEqual(saved_content, content)

    def test_save_empty_text_file(self):
        """Test saving an empty text file."""
        test_file = os.path.join(self.test_dir, "empty.txt")
        content = ""

        with open(test_file, "w") as f:
            f.write(content)

        self.assertTrue(os.path.exists(test_file))
        with open(test_file, "r") as f:
            saved_content = f.read()
        self.assertEqual(saved_content, content)

    def test_overwrite_existing_text_file(self):
        """Test overwriting an existing text file."""
        test_file = os.path.join(self.test_dir, "overwrite.txt")
        original_content = "Original content"
        new_content = "New content"

        with open(test_file, "w") as f:
            f.write(original_content)

        with open(test_file, "w") as f:
            f.write(new_content)

        with open(test_file, "r") as f:
            saved_content = f.read()
        self.assertEqual(saved_content, new_content)


if __name__ == "__main__":
    unittest.main()
