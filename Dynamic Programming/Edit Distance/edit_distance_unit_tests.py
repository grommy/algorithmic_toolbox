import unittest
from edit_distance import edit_distance


class EditDistance(unittest.TestCase):
    def test(self):
        for first_string, second_string, answer in (
            ("ab", "ab", 0),
            ("ab", "abc", 1),
            ("abc", "ab", 1),
            ("", "", 0),
            ("short", "ports", 3),
            ("editing", "distance", 5),
            ("a" * 100, "a" * 100, 0),
            ("ab" * 50, "ba" * 50, 2),
            ("d" * 2 + "ab", "ab" + "c" * 3, 5),
        ):
            self.assertEqual(answer, edit_distance(first_string, second_string))


if __name__ == '__main__':
    unittest.main()
