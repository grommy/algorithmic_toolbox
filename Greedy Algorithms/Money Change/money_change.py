# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins_10 = int(money/10)
    not_10 = money % 10

    coins_5 = int(not_10 / 5)
    coins_1 = not_10 % 5

    return coins_10 + coins_5 + coins_1


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
