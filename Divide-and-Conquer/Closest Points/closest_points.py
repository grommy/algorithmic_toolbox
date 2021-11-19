# python3
import math
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance(sorted_points, min_dist=None):
    if len(sorted_points) < 2:
        return float("inf")
    elif len(sorted_points) == 2:
        return math.sqrt(distance_squared(sorted_points[0], sorted_points[1]))
    else:
        middle_idx = math.ceil(len(sorted_points) / 2)
        left_points = sorted_points[: middle_idx]
        min_in_left = minimum_distance(left_points)
        right_points = sorted_points[middle_idx:]
        min_in_right = minimum_distance(right_points)
        min_dist = min(min_in_left, min_in_right)

        most_left_x = left_points[len(left_points) - 1].x
        least_right_x = right_points[0].x

        merge_candidates = []
        left_idx = len(left_points) - 1
        while left_idx >= 0 and least_right_x - left_points[left_idx].x < min_dist:
            merge_candidates.append(('l', left_points[left_idx]))
            left_idx -= 1

        right_idx = 0
        while right_idx < len(right_points) and right_points[right_idx].x - most_left_x < min_dist:
            merge_candidates.append(('r', right_points[right_idx]))
            right_idx += 1

        merge_candidates = sorted(merge_candidates, key=lambda p: p[1].y)
        for idx in range(len(merge_candidates)):
            side1, point1 = merge_candidates[idx]
            for side2, point2 in merge_candidates[idx+1: idx+8]:
                if side1 != side2:
                    new_dist = math.sqrt(distance_squared(point1, point2))
                    if new_dist < min_dist:
                        min_dist = new_dist

        return min_dist


def minimum_distance_squared(points):
    sorted_points = list(sorted(points, key=lambda p: p.x))
    return minimum_distance(sorted_points) ** 2


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    # input_points = [Point(1, 0), Point(5, 0), Point(3, 0), Point(10, 0)]
    # input_points = [Point(x=0, y=1), Point(x=0, y=2), Point(x=-2, y=0), Point(x=0, y=0), Point(x=0, y=-2)]

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
