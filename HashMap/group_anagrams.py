"""
思路: 主要利用 set特性存储元素的字符串以及出现次数，然后通过
其内存地址映射到group当前组合的对应的组序。

failure:
1. forzenset可以作为hashable key， 这样就可以不用存储patterns，并且可以直接得等pattern对应的组别
2. forzedset 接受 dict.items() 取值
3. set的一些用法
set.add, set == set, tuple 作为set的key.
"""

from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 0:
        return []
    if len(strs) == 1:
        return [[strs[0]]]
    pattern_to_group = {}
    for idx, item in enumerate(strs):
        cur_count = dict()
        for char in item:
            if char in cur_count:
                cur_count[char] += 1
            else:
                cur_count[char] = 1
        cur_pattern = frozenset(cur_count.items())
        if cur_pattern not in pattern_to_group:
            pattern_to_group[cur_pattern] = []
        pattern_to_group[cur_pattern].append(item)
    return [value for key, value in pattern_to_group.items()]


def normalize(groups):
    return sorted(
        [sorted(group) for group in groups]
    )


def test_group_anagrams():
    test_cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [
                ["eat", "tea", "ate"],
                ["tan", "nat"],
                ["bat"]
            ]
        ),

        # Empty string
        (
            [""],
            [[""]]
        ),

        # Single character
        (
            ["a"],
            [["a"]]
        ),

        # No anagrams
        (
            ["abc", "def", "ghi"],
            [
                ["abc"],
                ["def"],
                ["ghi"]
            ]
        ),

        # All strings are anagrams
        (
            ["abc", "bca", "cab", "cba"],
            [
                ["abc", "bca", "cab", "cba"]
            ]
        ),

        # Duplicate strings
        (
            ["abc", "abc", "bca"],
            [
                ["abc", "abc", "bca"]
            ]
        ),

        # Different character counts
        (
            ["a", "aa", "aaa"],
            [
                ["a"],
                ["aa"],
                ["aaa"]
            ]
        ),

        # Repeated characters
        (
            ["aab", "aba", "baa", "abb"],
            [
                ["aab", "aba", "baa"],
                ["abb"]
            ]
        ),

        # Multiple empty strings
        (
            ["", "", "a"],
            [
                ["", ""],
                ["a"]
            ]
        ),

        # Two larger groups
        (
            ["listen", "silent", "enlist", "google", "gogole"],
            [
                ["listen", "silent", "enlist"],
                ["google", "gogole"]
            ]
        ),
    ]

    for i, (strs, expected) in enumerate(test_cases, start=1):
        result = group_anagrams(strs)

        assert normalize(result) == normalize(expected), (
            f"Test {i} failed:\n"
            f"input = {strs}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(f"Test {i} passed")

    print("\nAll tests passed!")




