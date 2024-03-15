"""
Given a string, determine the length of the longest palindrome that can be constructed using the characters from the string. You don't need to return the palindrome itself, just its maximum possible length.

Time Complexity: O(n) loop through the string then loop through the hashmap which coule be O(n) size
Space Complexity: O(1) if we limit the character set in any way (O(26) for lower case chars for example)
"""


class Solution:
    def function_name(self, s):
        char_freq = {}
        length = 0
        for letter in s:
            char_freq[letter] = char_freq.get(letter, 0) + 1

        oddFound = False
        for freq in char_freq.values():
            # even frequency number - we can add all instances of this character to our palindrome
            if freq % 2 == 0:
                length += freq
            # odd frequency we can add all but one instance of this charcter to our palindrome (basically always use an even number of this character)
            else:
                length += freq - 1
                oddFound = True
        # we can use exactly on additional instance from a character with an odd frequency as the middle character in our palindrome
        if oddFound:
            length += 1

        return length


def main():
    sol = Solution()
    print(sol.function_name("bananas"))
    print(sol.function_name("applepie"))
    print(sol.function_name("racecar"))


main()
