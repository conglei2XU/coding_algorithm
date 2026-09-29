from typing import List
from collections import deque


def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not len(matrix):
        return []
    left_boundary, top_boundary = 0, 0
    right_boundary, bottom_boundary = len(matrix[0]) - 1, len(matrix) - 1
    global_spiral_num = []
    while left_boundary <= right_boundary and top_boundary <= bottom_boundary:
        for i in range(left_boundary, right_boundary + 1):
            global_spiral_num.append(matrix[top_boundary][i])
        for j in range(top_boundary + 1, bottom_boundary + 1):
            global_spiral_num.append(matrix[j][right_boundary])
        if top_boundary != bottom_boundary:
            for i in range(right_boundary - 1, left_boundary - 1, -1):
                global_spiral_num.append(matrix[bottom_boundary][i])
        if left_boundary != bottom_boundary:
            for j in range(bottom_boundary - 1, top_boundary, -1):
                global_spiral_num.append(matrix[j][left_boundary])
        left_boundary += 1
        top_boundary += 1
        right_boundary -= 1
        bottom_boundary -= 1
    return global_spiral_num


def test_spiral_order():
    test_cases = [
        # 2 x 2
        (
            [
                [1, 2],
                [3, 4]
            ],
            [1, 2, 4, 3]
        ),

        # 2 x 3
        (
            [
                [1, 2, 3],
                [4, 5, 6]
            ],
            [1, 2, 3, 6, 5, 4]
        ),

        # 3 x 2
        (
            [
                [1, 2],
                [3, 4],
                [5, 6]
            ],
            [1, 2, 4, 6, 5, 3]
        ),

        # Larger square matrix
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ],
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        ),

        # Negative numbers
        (
            [
                [-1, -2, -3],
                [-4, -5, -6]
            ],
            [-1, -2, -3, -6, -5, -4]
        ),
    ]

    for i, (matrix, expected) in enumerate(test_cases, start=1):
        result = spiral_order(matrix)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"matrix = {matrix}\n"
            f"expected = {expected}\n"
            f"actual = {result}"
        )

        print(f"Test {i} passed: {result}")

    print("\nAll tests passed!")
