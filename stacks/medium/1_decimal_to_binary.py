"""
Given a positive integer n, write a function that returns its binary equivalent as a string. The function should not use any in-built binary conversion function.

Time Complexity:
Space Complexity:
"""


class Solution:
    def decimal_to_binary(self, decimal):
        stack = []

        # dividing and modding this way gets us a list of bits from least to most significant bit
        while decimal > 0:
            # push the remainder of the number divided by 2 onto the stack
            stack.append(decimal % 2)
            # integer (floor) divide the number by 2
            decimal //= 2

        # we reverse the list at the end to get the binary representation in the proper order (most to least significant bit)
        return "".join(str(i) for i in reversed(stack))


def main():
    sol = Solution()
    print(sol.decimal_to_binary(5))
    print(sol.decimal_to_binary(11))
    print(sol.decimal_to_binary(18))


main()
