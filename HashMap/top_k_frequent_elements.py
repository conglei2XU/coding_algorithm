"""
思路：
遍历nums，使用freq_dict 记录每个元素出现的频率，同时利用index list[set]
记录出现频率对应的字母，最后取前index 前k个元素 为最终结果

[set] * 引用复制的问题；
建立 index record 时，使用额外的空间增加程序的可读性和操作的规范性；
可读性，操作性应该优于极致的性能优化；
"""

from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq_count = {}
    freq_record: List[set] = [set() for idx in range(len(nums) + 1)]
    for idx, num in enumerate(nums):
        if num in freq_count:
            freq = freq_count[num] + 1
            freq_count[num] = freq
            is_new = False
        else:
            freq = 1
            freq_count[num] = freq
            is_new = True
        if is_new:
            freq_record[freq].add(num)
        else:
            freq_record[freq - 1].remove(num)
            freq_record[freq].add(num)

    global_result = []
    for i in freq_record[::-1]:
        if len(i):
            global_result = global_result + list(i)
            k -= 1
        if k == 0:
            break

    return global_result


def test_top_k_frequent():
    test_cases = [
        # Basic case
        (
            [1, 1, 1, 2, 2, 3],
            2,
            {1, 2},
        ),

        # Single element
        (
            [1],
            1,
            {1},
        ),

        # All elements have different frequencies
        (
            [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],
            3,
            {1, 2, 3},
        ),

        # Negative numbers
        (
            [-1, -1, -1, -2, -2, -3],
            2,
            {-1, -2},
        ),

        # Zero included
        (
            [0, 0, 0, 1, 1, 2],
            2,
            {0, 1},
        ),

        # k equals number of unique elements
        (
            [1, 1, 2, 2, 3],
            3,
            {1, 2, 3},
        ),

        # One value dominates
        (
            [5, 5, 5, 5, 5, 2, 3, 4],
            1,
            {5},
        ),

        # Larger frequencies
        (
            [4, 4, 4, 4, 3, 3, 3, 2, 2, 1],
            2,
            {4, 3},
        ),
    ]

    for i, (nums, k, expected) in enumerate(test_cases, start=1):
        result = top_k_frequent(nums, k)

        assert len(result) == k, (
            f"Test {i} failed:\n"
            f"nums = {nums}\n"
            f"k = {k}\n"
            f"expected {k} elements\n"
            f"actual = {result}"
        )

        assert set(result) == expected, (
            f"Test {i} failed:\n"
            f"nums = {nums}\n"
            f"k = {k}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(f"Test {i} passed: {result}")

    print("\nAll tests passed!")

