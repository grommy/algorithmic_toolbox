# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]
    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


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


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    DIV = 10
    mod_sequence = get_mod_sequence(DIV)
    len_mod_sequence = len(mod_sequence)

    full_seq_to = int((to_index+0) / len_mod_sequence)
    full_seq_from = int((from_index+0) / len_mod_sequence)

    # full loop diff
    loop_sum = sum(mod_sequence) % DIV
    full_loop_sum = loop_sum * (full_seq_to - full_seq_from - 1) % DIV
    to_index -= (full_seq_to - full_seq_from - 1) * len_mod_sequence

    from_index_mode = from_index % len_mod_sequence
    diff = to_index - from_index

    if diff < len_mod_sequence - from_index_mode:
        diff_sum = sum(mod_sequence[from_index_mode: from_index_mode+diff+1]) % DIV
        return (full_loop_sum + diff_sum) % DIV

    else:
        last_seq_sum = sum(mod_sequence[from_index_mode:]) % DIV

        first_numbers = diff - (len_mod_sequence - from_index_mode)
        first_numbers_sum = sum(mod_sequence[:first_numbers+1]) % DIV

        return (full_loop_sum + last_seq_sum + first_numbers_sum) % DIV


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    # print(last_digit_of_the_sum_of_fibonacci_numbers_again_naive(7, 128))
    # print(last_digit_of_the_sum_of_fibonacci_numbers_again(7, 128))

    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
