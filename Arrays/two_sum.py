"""
思路：
朴素版：使用排序加二分查找的方法(nlogn)
sort the array first, then use binary search to find the complement of each number.
o(n):
using mapping to store value and its index of the array
"""


def binary_search(arr, start, end, target):
    if start > end:
        return
    if start == end:
        if arr[start][1] == target:
            return start
    mid = (start + end) // 2
    if arr[mid][1] == target:
        return mid
    elif arr[mid][1] < target:
        start = mid + 1
    else:
        end = mid - 1

    return binary_search(arr, start, end, target)


def two_sum(arr, target):
    nums = [(idx, value) for idx, value in enumerate(arr)]
    nums.sort(key=lambda x: x[1])
    for idx in range(len(arr) - 1):
        target_ = target - nums[idx][1]
        target_idx = binary_search(nums, idx + 1, len(nums) - 1, target_)
        if target_idx:
            return [nums[idx][0], nums[target_idx][0]]
def two_sum_plus(arr, target):
    # handle duplicate values in the array
    value_idx = {}
    for idx, value in enumerate(arr):
        if value not in value_idx:
            value_idx[value] = [idx]
        else:
            value_idx[value].append(idx)
    for idx, value in enumerate(arr):
        complement_num = target - value
        complement_idx = value_idx.get(complement_num, None)
        if complement_idx is None:
            continue
        if len(complement_idx) > 1:
            if complement_idx[0] == idx:
                return [idx, complement_idx[1]]
            else:
                return [idx, complement_idx[0]]
        else:
            if complement_idx[0] != idx:
                return [idx, complement_idx[0]]



def test_two_sum():
    test_cases = [
        # 普通情况
        ([4, 7, 1, 9, 3], 10),

        # 最前面的两个元素
        ([2, 7, 11, 15], 9),

        # 负数
        ([-3, 4, 3, 90], 0),

        # 重复数字
        ([3, 3], 6),

        # 0
        ([0, 4, 3, 0], 0),

        # 正数 + 负数
        ([-10, -2, 4, 8, 12], 2),

        # 答案在数组末尾
        ([1, 2, 3, 10, 20], 30),
    ]

    for i, (arr, target) in enumerate(test_cases, start=1):
        result = two_sum_plus(arr, target)

        assert result is not None, (
            f"Test {i} failed: returned None"
        )

        assert len(result) == 2, (
            f"Test {i} failed: expected 2 indices, got {result}"
        )

        idx1, idx2 = result

        assert idx1 != idx2, (
            f"Test {i} failed: used the same element twice"
        )

        assert 0 <= idx1 < len(arr), (
            f"Test {i} failed: index {idx1} out of range"
        )

        assert 0 <= idx2 < len(arr), (
            f"Test {i} failed: index {idx2} out of range"
        )

        assert arr[idx1] + arr[idx2] == target, (
            f"Test {i} failed:\n"
            f"arr = {arr}\n"
            f"target = {target}\n"
            f"result = {result}\n"
            f"{arr[idx1]} + {arr[idx2]} != {target}"
        )

        print(
            f"Test {i} passed: "
            f"{arr[idx1]} + {arr[idx2]} = {target}, "
            f"indices = {result}"
        )

    print("\nAll tests passed!")


test_two_sum()
