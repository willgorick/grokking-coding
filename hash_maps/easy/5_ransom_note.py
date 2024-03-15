"""
Given two strings, one representing a ransom note and the other representing the available letters from a magazine, determine if it's possible to construct the ransom note using only the letters from the magazine. Each letter from the magazine can be used only once.

Time Complexity: O(n+k) where n is the length of the magazine, k is the length of the ransom note
Space Complexity: O(1) for the fixed size of the english alphabet (if not fixed it would be O(n) the length of the magazine)
"""


class Solution:
    def ransome_note(self, ransomNote, magazine):
        char_freq = {}
        for letter in magazine:
            char_freq[letter] = char_freq.get(letter, 0) + 1

        for letter in ransomNote:
            if char_freq.get(letter, 0) > 0:
                char_freq[letter] -= 1
            else:
                return False
        return True


def main():
    sol = Solution()
    print(sol.ransome_note("hello", "hellworld"))
    print(sol.ransome_note("notes", "stoned"))
    print(sol.ransome_note("apple", "pale"))


main()
