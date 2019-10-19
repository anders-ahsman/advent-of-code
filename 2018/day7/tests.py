import unittest

from main import part1, part2

class Tests(unittest.TestCase):
    def test_part1_returns_expected_answer(self):
        self.assertEqual(part1(), 'AHJDBEMNFQUPVXGCTYLWZKSROI')

    def test_part2_returns_expected_answer(self):
        self.assertEqual(part2(), 1031)

if __name__ == '__main__':
    unittest.main()
