"""
Given a non-negative integer represented as a string num and an integer k, delete k digits from num to obtain the smallest possible integer. Return this minimum possible integer as a string.


Time Complexity: O(n) - append and pop each digit at most once
Space Complexity: O(n) - O(n) for the stack 
"""


class Solution:
    def remove_k_digits(self, num, k):
        stack = []
        for digit in num:
            # basically as long as there are larger digits on the stack than the current and we have k left, pop them
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            # add current digit to stack
            stack.append(digit)

        if k > 0:
            # truncate the final k digits
            stack = stack[:-k]
        # join the digits together
        digit_str = "".join(stack)
        # strip any leading 0's
        return digit_str.lstrip("0")


def main():
    sol = Solution()
    print(sol.remove_k_digits("1432219", 3))
    print(sol.remove_k_digits("10200", 1))
    print(sol.remove_k_digits("1901042", 4))


main()
