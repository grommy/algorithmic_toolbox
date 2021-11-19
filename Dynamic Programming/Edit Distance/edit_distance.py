# python3
"""
Given two strings of length at most 100,
compute the minimum number of single symbol insertions, deletions, and substitutions
to transform one string into the other one.

short->hort->port->ports
"""


def print_matr(matr):
    for row in matr:
        print(row)


def diff(a, b):
    return 0 if a == b else 1


def edit_distance(first_string, second_string):
    columns_num = len(second_string)+1
    rows_num = len(first_string)+1
    matr = [[0 for col in range(columns_num)] for row in range(rows_num)]
    for i in range(1, rows_num):
        matr[i][0] = i
    for j in range(1, columns_num):
        matr[0][j] = j

    # print_matr(matr)

    for i in range(1, rows_num):
        for j in range(1, columns_num):
            matr[i][j] = min([
                matr[i-1][j-1] + diff(first_string[i-1], second_string[j-1]),
                matr[i-1][j] + 1,
                matr[i][j-1] + 1
            ])
    # print_matr(matr)

    return matr[-1][-1]


if __name__ == "__main__":
    # a, b , answer = ("ab", "ab", 0)
    # a, b , answer = ("short", "ports", 3)
    # a, b , answer = ("editing", "distance", 5)
    # a, b, answer = ("d" * 2 + "ab", "ab" + "c" * 3, 5)
    # print(a)
    # print(b)
    # print(edit_distance(a, b))
    print(edit_distance(input(), input()))
