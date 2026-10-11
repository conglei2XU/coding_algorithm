"""
思路: 滑动窗口
从第一个字符开始滑动维护一个动态窗口，记录char的第一次出现位置，当窗口不符合约束时候，移动start使其满足约束。

两个边界需要注意：
1. 窗口不符合约束时候如何移动
2. 如何维护 freq dict 保证存储窗口内的值
"""
import random
import string
def character_replacement(s: str, k: int) -> int:
    start = 0
    max_len = 0
    char_freq = {}
    max_freq = 0
    for end, char in enumerate(s):
        char_freq[char] = char_freq.get(char, 0) + 1
        max_freq = max(max_freq, char_freq[char])
        while end - start + 1 - max_freq > k:
            char_freq[s[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)
    return max_len

def test_character_replacement():
    test_cases = [
        # Basic cases
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),

        # Single character
        ("A", 0, 1),

        # All characters are already the same
        ("AAAA", 0, 4),
        ("AAAA", 2, 4),

        # No replacements allowed
        ("ABCD", 0, 1),
        ("AABCC", 0, 2),

        # Enough replacements to make the whole string equal
        ("ABCD", 3, 4),

        # Best window is in the middle
        ("BAAAB", 1, 4),

        # Repeated groups
        ("AAABBB", 2, 5),

        # k is larger than needed
        ("ABC", 10, 3),

        # Empty string
        ("", 2, 0),

        # Longer mixed case
        ("AABCCBB", 2, 5),

        # Another useful sliding-window case
        ("ABBB", 1, 4),

        # Window needs to shrink
        ("ABCDEFFFG", 1, 4),
    ]

    for i, (s, k, expected) in enumerate(test_cases, start=1):
        result = character_replacement(s, k)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"s = {repr(s)}\n"
            f"k = {k}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(
            f"Test {i} passed: "
            f"s={repr(s)}, k={k}, result={result}"
        )

    print("\nAll tests passed!")

