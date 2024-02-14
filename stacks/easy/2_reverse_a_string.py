"""
Given a string, write a function that uses a stack to reverse the string. The function should return the reversed string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque


class Solution:
    def reverse_string(self, s):
        string_queue = []
        result = []
        for letter in s:
            string_queue.append(letter)
        while string_queue:
            result.append(string_queue.pop())
        return "".join(result)


def main():
    sol = Solution()
    print(sol.reverse_string("Hello World!"))


main()
