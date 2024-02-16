"""
Given a string S, remove all adjacent duplicate characters recursively to generate the resultant string.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def remove_all_duplicates_recursively(self, s):
        stack = []
        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)


def main():
    sol = Solution()
    print(sol.remove_all_duplicates_recursively("abccba"))
    print(sol.remove_all_duplicates_recursively("foobar"))


main()
