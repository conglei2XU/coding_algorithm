"""
思路1：list + history minimum store
使用list作为栈的主体结构。由于元素只在列表尾部进行插入和删除。因此push和pop操作都可以达到O(1）
普通栈查找最小值的时候，需要遍历整个栈，时间复杂度未O(n).为了让get min 达到O（1），需要额外保存
栈在变化过程中的状态。使用列表同步的保存当前栈对应最小值。
push新元素时，记录栈状态变化以及对应的minimum
pop元素时，取得pop后栈状态对应的minimum

因此，每次栈状态发生变化时，都可以在O(1)时间获取最小值。

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def test_min_stack():
    # Case 1: Basic example
    stack = MinStack()

    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2

    print("Test 1 passed")

    # Case 2: Minimum keeps decreasing
    stack = MinStack()

    stack.push(5)
    assert stack.getMin() == 5

    stack.push(4)
    assert stack.getMin() == 4

    stack.push(3)
    assert stack.getMin() == 3

    stack.push(2)
    assert stack.getMin() == 2

    print("Test 2 passed")

    # Case 3: Minimum should recover after pop
    stack = MinStack()

    stack.push(3)
    stack.push(2)
    stack.push(1)

    assert stack.getMin() == 1

    stack.pop()
    assert stack.getMin() == 2

    stack.pop()
    assert stack.getMin() == 3

    print("Test 3 passed")

    # Case 4: Duplicate minimum values
    stack = MinStack()

    stack.push(2)
    stack.push(1)
    stack.push(1)

    assert stack.getMin() == 1

    stack.pop()
    assert stack.getMin() == 1

    stack.pop()
    assert stack.getMin() == 2

    print("Test 4 passed")

    # Case 5: Negative values
    stack = MinStack()

    stack.push(-1)
    stack.push(-5)
    stack.push(-3)

    assert stack.getMin() == -5
    assert stack.top() == -3

    stack.pop()

    assert stack.top() == -5
    assert stack.getMin() == -5

    print("Test 5 passed")

    # Case 6: Minimum is not always at the top
    stack = MinStack()

    stack.push(1)
    stack.push(5)
    stack.push(3)
    stack.push(4)

    assert stack.getMin() == 1
    assert stack.top() == 4

    stack.pop()
    assert stack.getMin() == 1

    stack.pop()
    assert stack.getMin() == 1

    print("Test 6 passed")

    # Case 7: Push after several pops
    stack = MinStack()

    stack.push(5)
    stack.push(2)
    stack.push(8)

    assert stack.getMin() == 2

    stack.pop()
    stack.pop()

    assert stack.getMin() == 5

    stack.push(1)

    assert stack.getMin() == 1
    assert stack.top() == 1

    print("Test 7 passed")

    print("\nAll tests passed!")