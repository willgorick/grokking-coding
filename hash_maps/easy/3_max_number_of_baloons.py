"""
Given a string, determine the maximum number of times the word "balloon" can be formed using the characters from the string. Each character in the string can be used only once.

Time Complexity: O(n) one loop to populate the hashmap and then constant time operations for 5 letters
Space Complexity: O(1) because only the english alphabet is considered ( O(26) -> O(1))
"""


class Solution:
    def max_number_of_baloons(self, s):
        max_baloons = float("inf")
        letter_count = {}

        for letter in s:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        max_baloons = min(letter_count.get("b", 0), max_baloons)
        max_baloons = min(letter_count.get("a", 0), max_baloons)
        max_baloons = min(letter_count.get("l", 0) // 2, max_baloons)
        max_baloons = min(letter_count.get("o", 0) // 2, max_baloons)
        max_baloons = min(letter_count.get("n", 0), max_baloons)

        return max_baloons


def main():
    sol = Solution()
    print(sol.max_number_of_baloons("balloonballoon"))
    print(sol.max_number_of_baloons("bbaall"))
    print(sol.max_number_of_baloons("balloonballoooon"))


main()
