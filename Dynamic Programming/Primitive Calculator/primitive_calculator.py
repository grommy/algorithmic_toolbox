# python3

"""
Find the minimum number of operations needed to get
a positive integer n from 1 using only three operations:
add 1, multiply by 2, and multiply by 3.

Input. An integer 1 ≤ n ≤ 106.

Output. In the first line, output the minimum number k
of operations needed to get n from 1.
In the second line, output a sequence of intermediate numbers.
That is, the second line should contain positive integers a0,a1,…,ak
such that a0=1, ak=n,
and for all 1≤i≤k, ai is equal to either ai−1+1, 2ai−1, or 3ai−1.
If there are many such sequences, output any one of them.
"""


def minus_one(x):
    if x >= 1:
        return int(x-1)


def divide2(x):
    if x % 2 == 0:
        return int(x / 2)


def divide3(x):
    if x % 3 == 0:
        return int(x / 3)


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    reversed_ops = [minus_one, divide2, divide3]
    results = {0: []}
    for curr in range(1, n+1):
        min_ops = float('inf')
        best_prev_num = 0.1
        for reversed_op in reversed_ops:
            prev_num = reversed_op(curr)
            if prev_num in results:
                if len(results[prev_num]) + 1 < min_ops:
                    min_ops = len(results[prev_num]) + 1
                    best_prev_num = prev_num
        results[curr] = results[best_prev_num][:] + [curr]
    return results[n]


if __name__ == '__main__':
    input_n = int(input())
    # input_n = 99
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
