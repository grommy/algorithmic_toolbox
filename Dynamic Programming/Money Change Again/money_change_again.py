# python3
"""
Compute the minimum number of coins needed to change the given value
 into coins with denominations 1, 3, and 4.
"""


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    possible_coins = [1, 3, 4]
    num_coins_needed = {
        0: 0
    }
    for curr_amount in range(1, money + 1):
        min_coins = float('inf')
        for coin in possible_coins:
            if (curr_amount - coin >= 0) and (num_coins_needed[curr_amount - coin] + 1 < min_coins):
                min_coins = num_coins_needed[curr_amount - coin] + 1
        num_coins_needed[curr_amount] = min_coins
    return num_coins_needed[money]


if __name__ == '__main__':
    amount = int(input())
    # amount = 6
    print(change(amount))
