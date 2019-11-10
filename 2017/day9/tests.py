import unittest
from main import get_score_and_size

class Tests(unittest.TestCase):
    def test_get_score_and_size_returns_expected_score(self):
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
                score, _ = get_score_and_size(line)
                self.assertEqual(score, expected_score, line)

    def test_get_score_and_size_returns_expected_size(self):
        for line, expected_size in [
            ('<>', 0),
            ('<random characters>', 17),
            ('<<<<>', 3),
            ('<{!>}>', 2),
            ('<!!>', 0),
            ('<!!!>>', 0),
            ('<{o"i!a,<{i<a>', 10),
        ]:
            with self.subTest():
                _, size = get_score_and_size(line)
                self.assertEqual(size, expected_size, line)

if __name__ == '__main__':
    unittest.main()