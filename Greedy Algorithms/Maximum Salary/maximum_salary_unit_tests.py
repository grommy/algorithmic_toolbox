import unittest
from random import randint
from maximum_salary import largest_number_naive, largest_number


class TestLargestNumber(unittest.TestCase):
    def test_small(self):
        for numbers in [
            [1],
            [1, 2],
            [1000, 100, 10],
            [511, 51, 51],
            [56, 5, 6, 556, 566, 666, 665, 656],
            [2, 21],
            [1, 12],
            [2, 12],
            [2, 21],
            [2, 21, 23, 211, 213, 231, 232],
            [252, 25]
        ]:
            self.assertEqual(largest_number(numbers),
                             largest_number_naive(numbers))

    def test_large(self):
        for n in [2, 5, 10, 100]:
            for max_value in [1000, 10000]:
                numbers = [randint(1, max_value) for _ in range(n)]
                largest_number(numbers)


if __name__ == '__main__':
    unittest.main()
