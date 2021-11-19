# python3
"""
NOTE: how big is difference in speed between recurrent and loop algo
"""

def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n
    else:
        l: list = [1, 1]
        while len(l) != n:
            l.append(l[-2] + l[-1])
        return l[-1]


if __name__ == '__main__':
    input_n = int(input())
    # print(fibonacci_number_naive(input_n))
    print(fibonacci_number(input_n))
