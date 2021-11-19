# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        l: list = [1, 1]
        while len(l) != n:
            l.append(l[-2] + l[-1])
        return l[-1]


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    # calculate mod sequence
    initial_sequence = [0, 1]
    compete_sequence = []
    sequence_completed = False
    i = 2
    seq_possible_length = 2
    seq_matching_j = 0
    while not sequence_completed:
        mod = fibonacci_number(i) % m
        initial_sequence.append(mod)
        i += 1
        if mod == initial_sequence[seq_matching_j]:
            compete_sequence.append(mod)
            seq_matching_j += 1
        else:
            seq_matching_j = 0
            seq_possible_length = len(initial_sequence)
        sequence_completed = seq_possible_length == seq_matching_j

    mod_sequence = initial_sequence[:seq_possible_length]

    return mod_sequence[n % len(mod_sequence)]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
