"""
version 1:
排序后检查相邻两个元素的大小
version 2：
使用hash map
"""
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    seen_nums = set()
    for idx, value in enumerate(nums):
        if value in seen_nums:
            return True
        else:
            seen_nums.add(value)
    return False

def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    seen_nums: dict = {}
    for idx, value in enumerate(nums):
        most_recent_idx = seen_nums.get(value, None)
        if most_recent_idx is not None:
            distance = idx - most_recent_idx
            if distance <= k:
                return True
        seen_nums[value] = idx
    return False


def test_contains_nearby_duplicate():
    test_cases = [
        # Basic true case
        ([1, 2, 3, 1], 3, True),

        # Duplicate exists, but distance is too large
        ([1, 2, 3, 1, 2, 3], 2, False),

        # Adjacent duplicates
        ([1, 0, 1, 1], 1, True),

        # No duplicates
        ([1, 2, 3, 4], 3, False),

        # Empty list
        ([], 1, False),

        # Single element
        ([1], 1, False),

        # k = 0: two different indices can never have distance <= 0
        ([1, 1], 0, False),

        # Duplicate exactly k positions apart
        ([5, 6, 7, 5], 3, True),

        # Duplicate just outside k
        ([5, 6, 7, 8, 5], 3, False),

        # Multiple duplicates, at least one valid pair
        ([1, 2, 1, 3, 2], 2, True),

        # Negative numbers
        ([-1, -2, -3, -1], 3, True),

        # Same value appears many times
        ([4, 4, 4, 4], 1, True),
    ]

    for i, (nums, k, expected) in enumerate(test_cases, start=1):
        result = contains_nearby_duplicate(nums, k)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"nums = {nums}\n"
            f"k = {k}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(
            f"Test {i} passed: "
            f"nums={nums}, k={k}, result={result}"
        )

    print("\nAll tests passed!")