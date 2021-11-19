import unittest
from random import randint

from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            # type here
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def __generate_random(self, n, MAX_VAL=1000):
        starts = []
        ends = []
        for _ in range(n):
            start = randint(0, MAX_VAL)
            end = randint(start, MAX_VAL)
            starts.append(start)
            ends.append(end)

        points = [randint(0, MAX_VAL) for _ in range(n)]
        return starts, ends, points

    def test_random(self):
        for n in [10, 20, 100]:
            starts, ends, points = self.__generate_random(n)
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_large(self):
        n = 50000
        self.assertEqual(set(points_cover([5]*n, [7]*n, [1]*n)).pop(), 0)



if __name__ == '__main__':
    unittest.main()
