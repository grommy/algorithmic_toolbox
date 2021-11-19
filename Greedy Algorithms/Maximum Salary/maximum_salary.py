# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_greater_or_equal(digit, max_digit):
    digit_before = int(str(digit)+str(max_digit))
    digit_after = int(str(max_digit)+str(digit))
    return digit_before >= digit_after


def largestnumber(lst):
    answer = []

    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer


def largest_number(numbers):
    numbers_left = [str(num) for num in numbers]
    current_str = ''.join([str(i) for i in largestnumber(numbers_left)])
    return int(current_str)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    # input_numbers = [252, 25]
    print(largest_number(input_numbers))
