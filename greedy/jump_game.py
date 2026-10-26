"""
思路：递归加memorization
分析：问题转化为，判断以当前节点为起点，是否存在可以达到last node的路径，
由于数组中值的定义为max_step，对当前路径节点是否可以达到last node的判断，
转变为对于1-max_step路径上节点是否可以到达last node的判断，符合递归模式。
当递归到尾部时候可以判断路径的状态。
边界条件：
next_node ＞ 数组长度 返回True
value of next_node is 0 返回False
定义：
jump_ability[i] 代表第 i 个位置开始是否可以达到数组尾部
jumb_ability[i] = for step in nums[i]
                    jump_ability[i + step]

思路2：贪心算法
分析：当前问题并不需要计算所有路径的具体数值，只需要确定历史能到达的最大值，
如果最大值大于当前小标，则更新最大值，如果小于当前下标则不能到达当前节点及后续节点
DP/recursion: 从当前位置开始是否可以到达终点
greedy:  到目前为止，我最远可以到哪里
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    jump_ability_memory = {}

    def judge_jump_state(i):
        if i >= len(nums) - 1:
            jump_ability_memory[i] = True
            return True
        else:
            if nums[i] == 0:
                jump_ability_memory[i] = False
                return False
            if i in jump_ability_memory:
                return jump_ability_memory[i]
            else:
                for step in range(1, nums[i] + 1):
                    if judge_jump_state(i + step):
                        jump_ability_memory[i] = True
                        return True
                jump_ability_memory[i] = False
                return False

    return judge_jump_state(0)

def can_jump_greedy(nums: List[int]) -> bool:
    max_reach = 0
    for idx, value in enumerate(nums):
        if idx <= max_reach:
            max_reach = max(idx + value, max_reach)
        else:
            return False
    return True

def test_can_jump():
    test_cases = [
        # Basic reachable case
        ([2, 3, 1, 1, 4], True),

        # Basic unreachable case
        ([3, 2, 1, 0, 4], False),

        # Single element
        ([0], True),

        # Two elements, reachable
        ([1, 0], True),

        # Two elements, unreachable
        ([0, 1], False),

        # Large first jump
        ([5, 0, 0, 0, 0, 0], True),

        # Zero in the middle, but still reachable
        ([2, 0, 2, 0, 1], True),

        # Zero blocks all paths
        ([1, 1, 0, 1], False),

        # Multiple possible paths
        ([2, 5, 0, 0, 0, 1], True),

        # Must use earlier long jump
        ([3, 0, 0, 1], True),

        # Cannot get past a dead zone
        ([2, 0, 0, 1], False),

        # Exact jump to the end
        ([1, 2, 0, 0], True),

        # Many ones
        ([1, 1, 1, 1, 1], True),

        # Reachability grows gradually
        ([1, 2, 3, 0, 0, 0], True),

        # Large array with failure near the end
        ([4, 2, 0, 0, 1, 0, 1], False),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result_recursive = can_jump(nums)
        result_greedy = can_jump_greedy(nums)

        assert result_recursive == expected, (
            f"Recursive Test {i} failed:\n"
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"actual = {result_recursive}"
        )

        assert result_greedy == expected, (
            f"Greedy Test {i} failed:\n"
            f"nums = {nums}\n"
            f"expected = {expected}\n"
            f"actual = {result_greedy}"
        )

        print(
            f"Test {i} passed: "
            f"nums={nums}, result={expected}"
        )

    print("\nAll tests passed!")