# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        l: list = [1, 1]
        while len(l) != n:
            l.append(l[-2] + l[-1])
        return l[-1]


def get_mod_sequence(m):

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

    return mod_sequence


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    DIV = 10
    mod_sequence = get_mod_sequence(10)
    ns_last = mod_sequence[n % len(mod_sequence)]

    idx = n % len(mod_sequence)
    if idx < len(mod_sequence) - 2:
        next_idx = idx + 1
    else:
        next_idx = len(mod_sequence) - idx - 1
    ns_next_last = mod_sequence[next_idx]

    return (ns_last * ns_next_last) % DIV


if __name__ == '__main__':
    input_n = int(input())
    # input_n = 66
    # print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(input_n))
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
