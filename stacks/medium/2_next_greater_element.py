"""
Given an array, print the Next Greater Element (NGE) for every element.

The Next Greater Element for an element x is the first greater element on the right side of x in the array.

Elements for which no greater element exist, consider the next greater element as -1.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def next_greater_element(self, arr):
        stack = []
        res = [-1]*len(arr)
        for i in range(len(arr)-1, -1, -1):
            curr_val = arr[i]
            while stack:
                # peek at the top of the stack
                possible_NGE = stack[-1]
                # if the top of the stack is greater than current, that's the NGE
                if possible_NGE > curr_val:
                    res[i] = possible_NGE
                    break
                # if the value is to the right is less than curr_val then it can't the NGE for any index less than the current one (because either the curr_val would be or the value at the index is greater than curr_val so neither are the NGE)
                else:
                    stack.pop()
            # push each element onto the stack for the previous index to consider
            stack.append(curr_val)

        return res


def main():
    sol = Solution()
    print(sol.next_greater_element([4, 5, 2, 25]))
    print(sol.next_greater_element([13, 7, 6, 12]))
    print(sol.next_greater_element([1, 2, 3, 4, 5]))


main()
