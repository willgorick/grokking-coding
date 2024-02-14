"""
Given a string s containing (, ), [, ], {, and } characters. Determine if a given string of parentheses is balanced.

A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis in the correct order.

Time Complexity: O(n) each character in the string is considerd once
Space Complexity: O(n), all characters could be opening parentheses (also O(n/2) => O(n))
"""


class Solution:
    def is_balanced(self, s):
        open_set = set(["{", "[", "("])

        queue = []
        for char in s:
            if char in open_set:
                queue.append(char)
            else:
                if not queue:
                    return False
                last_open_char = queue.pop()
                if char == "]" and last_open_char != "[":
                    return False
                if char == ")" and last_open_char != "(":
                    return False
                if char == "}" and last_open_char != "{":
                    return False
        return len(queue) == 0


def main():
    sol = Solution()
    sol = Solution()

    test1 = "{[()]}"  # Should be valid
    test2 = "{[}]"   # Should be invalid
    test3 = "(]"     # Should be invalid

    print("Test 1:", sol.is_balanced(test1))
    print("Test 2:", sol.is_balanced(test2))
    print("Test 3:", sol.is_balanced(test3))


main()
