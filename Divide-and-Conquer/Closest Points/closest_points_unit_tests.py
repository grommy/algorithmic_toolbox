import unittest
from closest_points import minimum_distance_squared, minimum_distance_squared_naive, Point
from random import randint


class ClosestPoints(unittest.TestCase):
    def test_small(self):
        for points in (
            [Point(1, 0), Point(1, 1)],
            [Point(1, 0), Point(5, 0), Point(3, 0), Point(10, 0)],
            [Point(x=0, y=1), Point(x=0, y=2), Point(x=-2, y=0), Point(x=0, y=0), Point(x=0, y=-2)],
        ):
            self.assertAlmostEqual(minimum_distance_squared(points),
                                   minimum_distance_squared_naive(points),
                                   delta=1e-03)

    def test_random(self):
        for n in [2, 5, 10, 100]:
            for max_value in [1, 2, 3, 1000]:
                points = []
                for _ in range(n):
                    x = randint(-max_value, max_value)
                    y = randint(-max_value, max_value)
                    points.append(Point(x, y))

                # dist_naive = minimum_distance_squared_naive(points)
                # dist_my = minimum_distance_squared(points)
                # if abs(dist_naive - dist_my) > 0.001:
                #     print(points)
                self.assertAlmostEqual(minimum_distance_squared(points),
                                       minimum_distance_squared_naive(points),
                                       delta=1e-03)

    def test_large(self):
        points = [Point(1, 0), Point(2, 0)]
        for _ in range(10**5):
            points.append(Point(randint(3, 1000), randint(3, 1000)))

        minimum_distance_squared(points)


if __name__ == '__main__':
    unittest.main()
