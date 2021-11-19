# python3
"""
Given a set of gold bars of various weights and a backpack that can hold
at most W pounds, place as much gold as possible into the backpack.

Constraints. 1 ≤ W≤ 104. There are at most 103 gold bars,
the weight of each gold bar is at most 105.
"""
from sys import stdin


def print_matr(matr):
    for row in matr:
        print(row)


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    w_matr = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]

    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            w_matr[i][j] = max(w_matr[i-1][j], w_matr[i][j-1])
            curr_weight = weights[i-1]
            if curr_weight <= j:
                w_matr[i][j] = max((w_matr[i-1][j-curr_weight]+curr_weight,
                                    w_matr[i][j]))
    # print_matr(w_matr)
    return w_matr[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    # input_capacity, input_weights, _ = (10, (1, 4, 8), 9)
    # input_capacity, input_weights, _ = (20, (5, 7, 12, 18), 19)
    # input_capacity, input_weights, _ = (10, (3, 5, 3, 3, 5), 10)

    print(maximum_gold(input_capacity, input_weights))
