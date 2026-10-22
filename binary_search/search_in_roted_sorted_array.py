"""
思路1：顺序遍历算法
从左到右遍历数组，依次判断当前元素是否等于target。
如果找到则返回对应下标，否则返回-1.
时间复杂度：O(N)
空间复杂度：O(1)
思路2: 二分查找
数组经过旋转不再整体有序，但它是一个严格升序数组旋转得到。因此，对于搜索区间[left, right], 以mid
划分后，左右两部分至少有一部分仍然是有序的。
每轮二分查找执行一下判断：
1.判断哪一半是有序的
2.判断target是否位于有序部分之间
3. 在新的搜索区间中重复以上过程，直到找到target，或者left>right

"""

from typing import List


def search_burst(nums: List[int], target: int) -> int:
    for idx, value in enumerate(nums):
        if value == target:
            return idx
    return -1


def binary_search(left, right, target, nums):
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    # whether left part is sorted
    if nums[mid] >= nums[left]:
        if nums[left] <= target <= nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] <= target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return binary_search(left, right, target, nums)


def search(nums: List[int], target: int) -> int:
    return binary_search(0, len(nums) - 1, target, nums)


def test_search():
    test_cases = [
        # # Basic rotated array
        # ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        #
        # # Target does not exist
        # ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        #
        # # Single element, target exists
        # ([1], 1, 0),
        #
        # # Single element, target does not exist
        # ([1], 0, -1),
        #
        # # Not rotated
        # ([1, 2, 3, 4, 5], 4, 3),

        # Target at the beginning
        # ([5, 1, 2, 3, 4], 5, 0),

        # Target at the end
        ([5, 1, 2, 3, 4], 4, 4),

        # Rotation near the middle
        ([6, 7, 8, 1, 2, 3, 4, 5], 2, 4),

        # Target in the left sorted portion
        ([6, 7, 8, 1, 2, 3, 4, 5], 7, 1),

        # Target in the right sorted portion
        ([6, 7, 8, 1, 2, 3, 4, 5], 4, 6),

        # Two elements
        ([3, 1], 1, 1),

        # Two elements, missing target
        ([3, 1], 2, -1),

        # Negative numbers
        ([0, 1, 2, -4, -3, -2, -1], -3, 4),
    ]

    for i, (nums, target, expected) in enumerate(test_cases, start=1):
        result = search(nums, target)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"nums = {nums}\n"
            f"target = {target}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(
            f"Test {i} passed: "
            f"target={target}, index={result}"
        )

    print("\nAll tests passed!")
