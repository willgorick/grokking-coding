"""
Given a stack, sort it using only stack operations (push and pop).

You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The values in the stack are to be sorted in descending order, with the largest elements on top.

Time Complexity: O(n^2) - worst case is numbers are already sorted in input, meaning for each value we pop from the input stock we have to pop all values from the result stack in order to place it
Space Complexity: O(n) result stack
"""


class Solution:
    def function_name(self, stack):
        sorted_stack = []
        while stack:
            curr_val = stack.pop()
            while sorted_stack and sorted_stack[-1] > curr_val:
                stack.append(sorted_stack.pop())
            sorted_stack.append(curr_val)
        return sorted_stack


def main():
    sol = Solution()
    print(sol.function_name([34, 3, 31, 98, 92, 23]))
    print(sol.function_name([4, 3, 2, 10, 12, 1, 5, 6]))
    print(sol.function_name([20, 10, -5, -1]))


main()
