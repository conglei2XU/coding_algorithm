"""
思路暴力解法 1：
计算每一天卖出的利润，取最大值 o(n) o(n^2)
思路2：
保存一个base利润表，根据当前的价格和前一天价格的差值，得到一个利润表；
然后基于利润表的动态变化，找到连续累加最大的子数组
"""
from typing import List
def max_profit(prices: List):
    cur_max = 0
    for idx in range(len(prices) - 1):
        for idy in range(idx + 1, len(prices)):
            profit = prices[idy] - prices[idx]
            if profit > cur_max:
                cur_max = profit
    return cur_max

def max_profit_plus(prices: list):

    if len(prices) <= 1:
        return 0
    max_profit, cur_max_profit = 0, 0
    for idx in range(1, len(prices)):
        profit = prices[idx] - prices[idx-1]
        if cur_max_profit + profit > 0:
            cur_max_profit = cur_max_profit + profit
        else:
            cur_max_profit = profit
        max_profit = max(max_profit, cur_max_profit)
    return max_profit

def test_max_profit_plus():
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([2, 4, 1], 2),
        ([3, 3, 5, 0, 0, 3, 1, 4], 4),
        ([1], 0),
        ([], 0),
    ]

    for i, (prices, expected) in enumerate(test_cases, start=1):
        try:
            result = max_profit_plus(prices)
        except Exception as e:
            print(
                f"Test {i} ERROR\n"
                f"prices = {prices}\n"
                f"expected = {expected}\n"
                f"exception = {type(e).__name__}: {e}\n"
            )
            continue

        if result == expected:
            print(f"Test {i} PASSED: result = {result}")
        else:
            print(
                f"Test {i} FAILED\n"
                f"prices = {prices}\n"
                f"expected = {expected}\n"
                f"actual = {result}\n"
            )


test_max_profit_plus()






