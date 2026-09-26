from typing import List
from collections import deque

def spiral_order(matrix: List[List[int]]) -> List[int]:
    if not len(matrix):
        return []
    start_row, start_col = 0, 0
    boundary_height, boundary_width = len(matrix), len(matrix[0])
    global_spiral_num = []

    while start_col < boundary_width and start_col < boundary_height:
        bottom_row, left_column, right_column = deque(), deque(), deque()
        global_spiral_num.extend(matrix[start_row][start_col:boundary_width])
        for idx_row in range(start_row + 1, boundary_height):
            if idx_row < boundary_height - 1:
                left_column.appendleft(matrix[idx_row][start_col])
                right_column.append(matrix[idx_row][boundary_width - 1])
            else:
                for idx_col in range(start_col, boundary_width):
                    bottom_row.appendleft(matrix[idx_row][idx_col])
        spiral_travers_res = list(right_column + bottom_row + left_column)
        global_spiral_num.extend(spiral_travers_res)
        start_row += 1
        start_col += 1
        boundary_height -= 1
        boundary_width -= 1
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
                [1,  2,  3,  4],
                [5,  6,  7,  8],
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

