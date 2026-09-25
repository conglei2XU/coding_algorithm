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

