"""
Given a string, identify the position of the first character that appears only once in the string. If no such character exists, return -1.

Time Complexity: O(n) two loops over at most all chars in string
Space Complexity: O(1) given there is a limit on English letters (and on ASCII characters if we extend to that)
"""


class Solution:
    def first_nonrepeating_character(self, s):
        char_count = {}
        for char in s:
            # increment count for this char if already found, otherwise set to 1 (0 + 1)
            char_count[char] = char_count.get(char, 0) + 1
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        return -1


def main():
    sol = Solution()
    print(sol.first_nonrepeating_character("apple"))
    print(sol.first_nonrepeating_character("abcab"))
    print(sol.first_nonrepeating_character("abab"))


main()
