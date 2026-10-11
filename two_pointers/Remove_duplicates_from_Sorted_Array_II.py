"""
思路1：遍历+计数+原地删除
因为数组有序，相同的元素必定连续出现。遍历数组并记录当前元素的出现次数；前两次出现保留，超过两次则原地删除。
遇到新元素则重置计数。由于删除列表中间元素需要移动后续元素，最坏情况下时间复杂度可能达到 O(n²)。
知识点：
list remove by index
程序可优化的点：
返回值为长度，所以尝试不记录数组，指针遍历过滤超过2次出现的数；
新元素出现时将前一个数的长度加入总长度，最后加入当前轮的长度。
题目不仅仅要求返回长度还需要返回处理好的数组，因此需要条件元素交换的逻辑。

问题：
第一版设计时候，会对数组进行swap导致后续为访问的元素顺序发生变化。
在对list进行原地修改时候一定要小心，

双指针思路：
"""

from typing import List

def remove_duplicates(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    old_value = nums[0]
    traverse = 1
    count = 1
    while traverse < len(nums):
        if nums[traverse] == old_value:
            if count <= 1:
                count += 1
                traverse += 1
            else:
                del nums[traverse]
        else:
            old_value = nums[traverse]
            count = 1
            traverse += 1
    return len(nums)

def remove_duplicates_plus(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    start, traverse = 0, 1
    idx_in = traverse
    count = 1
    total_len = 0
    while traverse < len(nums):
        if nums[traverse] == nums[start]:
            if count <= 1:
                nums[idx_in] = nums[traverse]
                count += 1
                idx_in += 1

        else:
            start = traverse
            nums[idx_in] = nums[traverse]
            idx_in += 1
            count = 1
        traverse += 1
    return idx_in


def test_remove_duplicates():
    test_cases = [
        (
            [1, 1, 1, 2, 2, 3],
            5,
            [1, 1, 2, 2, 3],
        ),

        (
            [0, 0, 1, 1, 1, 1, 2, 3, 3],
            7,
            [0, 0, 1, 1, 2, 3, 3],
        ),

        # Empty array
        (
            [],
            0,
            [],
        ),

        # Single element
        (
            [1],
            1,
            [1],
        ),

        # Exactly two duplicates
        (
            [1, 1],
            2,
            [1, 1],
        ),

        # Three identical elements
        (
            [1, 1, 1],
            2,
            [1, 1],
        ),

        # All elements are the same
        (
            [2, 2, 2, 2, 2],
            2,
            [2, 2],
        ),

        # No duplicates
        (
            [1, 2, 3, 4, 5],
            5,
            [1, 2, 3, 4, 5],
        ),

        # Multiple groups with too many duplicates
        (
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            6,
            [1, 1, 2, 2, 3, 3],
        ),

        # Negative numbers
        (
            [-3, -3, -3, -2, -2, -1],
            5,
            [-3, -3, -2, -2, -1],
        ),

        # Mixed duplicate counts
        (
            [1, 1, 1, 1, 2, 3, 3, 4, 4, 4],
            7,
            [1, 1, 2, 3, 3, 4, 4],
        ),
    ]

    for i, (nums, expected_k, expected_nums) in enumerate(
        test_cases,
        start=1,
    ):
        original = nums.copy()

        k = remove_duplicates_plus(nums)

        assert k == expected_k, (
            f"Test {i} failed:\n"
            f"input = {original}\n"
            f"expected k = {expected_k}\n"
            f"actual k = {k}"
        )

        assert nums[:k] == expected_nums, (
            f"Test {i} failed:\n"
            f"input = {original}\n"
            f"expected nums[:k] = {expected_nums}\n"
            f"actual nums[:k] = {nums[:k]}"
        )

        print(
            f"Test {i} passed: "
            f"k={k}, nums[:k]={nums[:k]}"
        )

    print("\nAll tests passed!")


