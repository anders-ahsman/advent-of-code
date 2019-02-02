import unittest

from main import part1, part2

class Tests(unittest.TestCase):
    def test_part1_returns_expected_answer(self):
        self.assertEqual(part1(), 109143)

    def test_part2_returns_expected_answer(self):
        self.assertEqual(part2(), 506)

if __name__ == '__main__':
    unittest.main()
