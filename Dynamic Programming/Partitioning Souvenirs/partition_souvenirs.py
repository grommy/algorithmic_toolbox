# python3
"""
You and two of your friends have just returned back home
after visiting various countries.
Now you would like to evenly split all the souvenirs
that all three of you bought.

Input. A sequence of integers v1,v2,…,vn.
Output. Output 1, if it is possible to partition them into three subsets
with equal sums. Output 0 otherwise.

Constrains. 1≤n≤20, 1≤vi≤30 for all i.
"""
from sys import stdin


class KnapsackMultiple:

    @classmethod
    def is_possible_to_divide(cls, weights, n_pieces):
        all_sum = sum(weights)
        if all_sum % 3 != 0:
            return 0

        required_sum = int(all_sum / 3)
        available_weights = list([w for w in weights if w <= required_sum])
        available_weights = list(sorted(available_weights.copy()))
        w_matr = cls.knapsack(required_sum, available_weights)
        # cls.print_matr(w_matr, available_weights)

        possible_combos = [i for i in range(len(w_matr)) if w_matr[i][-1] == required_sum]
        # hint: no need to deconstruct the knapsack
        # possible_combos = cls.deconstruct_knapsack(w_matr, available_weights, required_sum)
        return int(len(possible_combos) >= n_pieces)

    @staticmethod
    def print_matr(matr, weights):
        weight_ = [0] + weights
        for i, row in enumerate(matr):
            print(weight_[i], row)

    @staticmethod
    def knapsack(capacity, weights):
        w_matr = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
        for i in range(1, len(weights) + 1):
            for j in range(1, capacity + 1):
                w_matr[i][j] = max(w_matr[i - 1][j], w_matr[i][j - 1])
                curr_weight = weights[i - 1]
                if curr_weight <= j:
                    if w_matr[i - 1][j - curr_weight] + curr_weight > w_matr[i][j]:
                        w_matr[i][j] = w_matr[i - 1][j - curr_weight] + curr_weight

        return w_matr

    @staticmethod
    def deconstruct_knapsack(w_matr, weights, required_capacity):
        combinations = 0
        weights_combo = []
        matched_i = [i for i in range(len(w_matr)) if w_matr[i][-1] == required_capacity]

        while len(matched_i) >= 1:
            if combinations >= 3:
                break

            i = matched_i[-1]
            j = len(w_matr[0]) - 1
            combo = []
            combo_idx = []
            while i > 0 and j > 0 and w_matr[i][j] > 0:
                if w_matr[i][j] >= weights[i-1]:
                    combo_idx.append(i)
                    combo.append(weights[i-1])
                    j -= weights[i-1]
                    i -= 1
                else:
                    i -= 1
            if sum(combo) == required_capacity:
                combinations += 1
                weights_combo.append(combo)
                for idx in combo_idx:
                    weights.pop(idx-1)
                    w_matr.pop(idx)
            else:
                idx = matched_i[-1]
                weights.pop(idx - 1)
                w_matr.pop(idx)
            matched_i = [i for i in range(len(w_matr)) if w_matr[i][-1] == required_capacity]

        print(weights_combo)
        return weights_combo


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    return KnapsackMultiple.is_possible_to_divide(values, 3)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    # input_values = 3, 6, 4, 1, 9, 6, 9, 1
    # input_values = 7,7,7
    print(partition3(input_values))
