import unittest

from main import part1

class Tests(unittest.TestCase):
    def test_part1_returns_expected_answer(self):
        self.assertEqual(part1(), 'AHJDBEMNFQUPVXGCTYLWZKSROI')

if __name__ == '__main__':
    unittest.main()
