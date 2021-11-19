# python3
from sys import stdin
"""
You are organizing an online lottery. To participate, 
a person bets on a single integer. You then draw several segments 
of consecutive integers at random. 
A participant’s payoff is proportional to the number of segments 
that contain the participant’s number. You need an efficient algorithm 
for computing the payoffs for all participants. 
A simple scan of the list of all ranges for each participant is too slow
since your lottery is very popular: you have thousands of participants 
and thousands of ranges.

Input: A list of n≤50000 segments and a list of m ≤ 50000 points.

Output: The number of segments containing each point.
"""


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover_(starts, ends, points):
    sorted_points = list(sorted(enumerate(points), key=lambda x: x[1]))
    not_started_ranges = list(sorted(zip(starts, ends), key=lambda x: x[0]))

    count = [0] * len(points)
    started_ranges = []
    ranges_idx = 0
    for p_idx, p in sorted_points:
        while ranges_idx < len(not_started_ranges) and \
                p >= not_started_ranges[ranges_idx][0]:
            started_ranges.append(not_started_ranges[ranges_idx])
            ranges_idx += 1

        for range in started_ranges[:]:
            if p > range[1]:
                started_ranges.remove(range)
            else:
                count[p_idx] += 1
    return count


def points_cover(starts, ends, points):
    count = [0] * len(points)
    master_list = []

    sorted_points = list(sorted(enumerate(points), key=lambda x: x[1]))
    # print(sorted_points)
    master_list.extend([(p, 'p') for p in points])
    master_list.extend([(s, 'l') for s in starts])
    master_list.extend([(e, 'r') for e in ends])

    master_list.sort()
    # print(master_list)

    p_idx = 0
    open_segments_count = 0
    for p_val, point_type in master_list:
        if point_type == 'l':
            open_segments_count += 1
        elif point_type == 'r':
            open_segments_count -= 1
            open_segments_count = max(open_segments_count, 0)
        else:
            count_idx = sorted_points[p_idx][0]
            count[count_idx] = open_segments_count
            p_idx += 1

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    # input_starts = [0, 5, 7]
    # input_ends = [5, 6, 10]
    # input_points = [6, 1, 11]
    #
    # output_count_naive = points_cover_naive(input_starts, input_ends, input_points)
    # print(*output_count_naive)
    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
