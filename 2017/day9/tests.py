import unittest
from main import get_score

class Tests(unittest.TestCase):
    def test_get_score(self):
        for line, expected_score in [
            ('{}', 1),
            ('{{{}}}', 6),
            ('{{},{}}', 5),
            ('{{{},{},{{}}}}', 16),
            ('{<{},{},{{}}>}', 1),
            ('{<a>,<a>,<a>,<a>}', 1),
            ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
            ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
            ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)
        ]:
            with self.subTest():
                self.assertEqual(get_score(line), expected_score, line)

if __name__ == '__main__':
    unittest.main()