"""
思路1：暴力遍历
依次从第一个字符到最后一个字符开始遍历，记录最长字串的长度。
时间复杂度o(n^2)
思路2: 滑动窗口算法
从第一个字符串开始滑动，记录滑动过程中每个字符串最近一次出现的位置，
当下一个字符串为重复字符时候更新滑动窗口的状态；
不需要记录路径上的char只需要维护一个当前长度即可；
char in last occur move start to right, then move end;
char not in last occur move end;

"""

def length_of_longest_substring(s: str) -> int:
    start = 0
    last_occur = {}
    max_len = 0
    for end, char in enumerate(s):
        if char in last_occur:
            start = max(start, last_occur[char] + 1)
        last_occur[char] = end
        cur_len = end - start + 1
        max_len = max(cur_len, max_len)
    return max_len


def test_length_of_longest_substring():
    test_cases = [
        # ("abcabcbb", 3),
        # ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
        ("abcdef", 6),
        ("aab", 2),
        ("tmmzuxt", 5),
        ("anviaj", 5),
        (" ", 1),
        ("  ", 1),
        ("a b c a", 3),
    ]

    for i, (s, expected) in enumerate(test_cases, start=1):
        result = length_of_longest_substring(s)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"s = {repr(s)}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(f"Test {i} passed: {repr(s)} -> {result}")

    print("\nAll tests passed!")

