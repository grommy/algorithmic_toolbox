# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]
    return sum(fibonacci_numbers) % 10


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


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    n = n + 1
    mod_sequence = get_mod_sequence(10)
    len_mod_sequence = len(mod_sequence)

    last_digit_of_sequence_sum = sum(mod_sequence) % 10
    total = (last_digit_of_sequence_sum * int(n / len(mod_sequence))) % 10  # 6

    last_n = n % len_mod_sequence
    sum_last_n = sum(mod_sequence[:last_n]) % 10

    return (total + sum_last_n) % 10


if __name__ == '__main__':
    input_n = int(input())
    # print(last_digit_of_the_sum_of_fibonacci_numbers_naive(input_n))
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
