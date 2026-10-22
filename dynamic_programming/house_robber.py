"""
思路1：递归+memorization的分方法
分析：路径的pattern符合以下模式：选取当前，然后选取加2或者加3为下一个位置值。由于房间的value为非负，所以最优路径是
先选择1或者2的其中一个。递归的top-bottom计算所有路径的值。
rub[i]选取当前房间后的最大值，由于递归过程存在许多重复的路径，需要设计一个数据结构存储历史路径结果。
递归的模式
rub[i] = num[i] + max(rub[i-2], rub[i-3)

思路2：bottom到top的动态规划方法
分析：从当前位置开始的最佳路径，是nums[i] + +2 位置与 +1位置的最大值
定义rub[i]为rub from i 的最大值，则rub[i]的状态转移为：
rub[i] = max(i + rub[i-2], rub[i-1])
从叶子开始往回回溯到开始找到最大值
"""
from typing import List


def rob(nums: List[int]) -> int:
    memorization = {}
    def rub_from(i):
        if i >= len(nums):
            return 0
        if i in memorization:
            return memorization[i]
        max_rub_next = max(rub_from(i + 2), rub_from(i + 3))
        memorization[i] = nums[i] + max_rub_next
        return memorization[i]

    rub_first = rub_from(0)
    rub_second = rub_from(1)
    return max(rub_first, rub_second)

def rob_db(nums: List) -> int:
    rub_value = [0] * (len(nums) + 2)
    i = len(nums) - 1
    while i >= 0:
        rub_value[i] = max(nums[i] + rub_value[i+2], rub_value[i+1])
        i -= 1
    return rub_value[0]



def test_rob():
    test_cases = [
        # Basic cases
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),

        # Empty list
        ([], 0),

        # Single house
        ([5], 5),

        # Two houses
        ([2, 7], 7),

        # Three houses
        ([2, 1, 4], 6),

        # All values are the same
        ([5, 5, 5, 5], 10),

        # Best choice is every other house
        ([10, 1, 10, 1, 10], 30),

        # Large value in the middle
        ([1, 2, 100, 2, 1], 102),

        # Choosing adjacent large-looking values is not allowed
        ([2, 100, 100, 2], 102),

        # More irregular pattern
        ([6, 7, 1, 30, 8, 2, 4], 41),

        # Zeros included
        ([0, 0, 0, 0], 0),

        # Alternating values
        ([1, 10, 1, 10, 1, 10], 30),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = rob_db(nums)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(f"Test {i} passed: nums={nums}, result={result}")

    print("\nAll tests passed!")
