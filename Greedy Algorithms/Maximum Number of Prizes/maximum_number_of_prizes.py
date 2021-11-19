# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    total_sum = 0
    next_val = 1
    while next_val <= n - total_sum:
        summands.append(next_val)
        total_sum += next_val
        next_val += 1
    if sum(summands) < n:
        summands[-1] = n - sum(summands[:-1])

    return summands


if __name__ == '__main__':
    # input_n = int(input())
    input_n = 100
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
