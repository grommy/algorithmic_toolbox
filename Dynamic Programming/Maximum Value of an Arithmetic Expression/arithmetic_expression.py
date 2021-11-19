# python3
"""
Parenthesize an arithmetic expression to maximize its value.
(8-5)*3 = 9
8-(5*3) = -7
Input. A string s=s0s1⋯s2n of length at most 29.
Each symbol at an even position of s is a digit (that is, an integer from 0 to 9)
while each symbol at an odd position is one of three operations from {+,−,∗}.

Output. The maximum value of the given arithmetic expression
among all possible orders of applying arithmetic operations.
"""


class ExpressionCalc:
    def __init__(self, expression):
        self.expression = expression
        self.__numbers, self.__ops = self.__parse(expression)

    def get_min_val(self):
        return self.__calc_min_and_max_expression_res()[0]

    def get_max_val(self):
        return self.__calc_min_and_max_expression_res()[1]

    @staticmethod
    def __create_none_2d_array(rows, columns, default_val=None):
        l = [default_val] * columns
        arr = []
        for i in range(rows):
            arr.append(l[:])
        return arr

    @staticmethod
    def __parse(expression):
        numbers = []
        ops = []
        even_idx = [idx for idx in range(len(expression)) if idx % 2 == 0]
        for idx in range(len(expression)):
            if idx in even_idx:
                numbers.append(expression[idx])
            else:
                ops.append(expression[idx])
        return numbers, ops

    def __calc_min_and_max_expression_res(self):
        arr_size = len(self.__numbers)
        min_arr = self.__create_none_2d_array(arr_size, arr_size)
        max_arr = self.__create_none_2d_array(arr_size, arr_size)
        for iter in range(arr_size):
            for col_idx in range(iter, arr_size):
                row_idx = col_idx - iter
                min_res, max_res = self.__calc_min_max_arr_vals(min_arr, max_arr, row_idx, col_idx)
                min_arr[row_idx][col_idx] = min_res
                max_arr[row_idx][col_idx] = max_res
        return min_arr[0][-1], max_arr[0][-1]

    def __calc_min_max_arr_vals(self, min_arr, max_arr, row_idx, col_idx):
        if row_idx == col_idx:
            num = int(self.__numbers[row_idx])
            return num, num
        else:
            expressions = []
            for idx in range(row_idx, col_idx):
                n1_max = max_arr[row_idx][idx]
                n2_max = max_arr[idx + 1][col_idx]

                n1_min = min_arr[row_idx][idx]
                n2_min = min_arr[idx + 1][col_idx]

                op = self.__ops[idx]

                expressions.append(f'{n1_max}{op}{n2_max}')
                expressions.append(f'{n1_max}{op}{n2_min}')
                expressions.append(f'{n1_min}{op}{n2_max}')
                expressions.append(f'{n1_min}{op}{n2_min}')

            results = [eval(expr) for expr in expressions]
            return min(results), max(results)


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    calc = ExpressionCalc(dataset)
    return calc.get_max_val()


if __name__ == "__main__":
    # expression, result = ("5-8+7*4-8+9", 200)
    # print(find_maximum_value(expression))
    print(find_maximum_value(input()))
