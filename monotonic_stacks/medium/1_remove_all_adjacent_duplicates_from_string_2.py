"""
You are given a string s and an integer k. Your task is to remove groups of identical, consecutive characters from the string such that each group has exactly k characters. The removal of groups should continue until it's no longer possible to make any more removals. The result should be the final version of the string after all possible removals have been made.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def remove_all_duplicates_recursively(self, s, k):
        stack = []
        # keep a stack with tuples representing the letter and its current count, if any character reaches a count of 3 remove it from the stack
        for letter in s:
            # update the count for this letter
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1
            # push the letter and a count of 1 to the stack
            else:
                stack.append([letter, 1])
            # if we have k in a row, remove them
            if stack[-1][1] == k:
                stack.pop()

        # join is multiplying each letter by its count
        return "".join(letter * count for letter, count in stack)


def main():
    sol = Solution()
    print(sol.remove_all_duplicates_recursively("abbbaaca", 3))
    print(sol.remove_all_duplicates_recursively("abbaccaa", 3))
    print(sol.remove_all_duplicates_recursively("abbacccaa", 3))


main()
