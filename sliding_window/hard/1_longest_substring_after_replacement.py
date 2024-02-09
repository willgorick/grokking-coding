"""
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Time Complexity: O(n) - each end character is evaluated once
Space Complexity: O(1) - technically O(26) for each lower case letter that could be stored in our dict but this asymptotically evaluates to O(1)
"""

from collections import defaultdict

class Solution:
    def longest_after_replacement(self, str1, k):
        start, max_len, max_repeat_letter_count = 0, 0, 0
        letter_frequency = defaultdict(int)

        for end in range(len(str1)):
            #add current letter to our frequency map
            curr_letter = str1[end]
            letter_frequency[curr_letter] += 1

            #check if addition of current letter causes it to be the max_repeat letter and increase that count if so
            #The only thing we need to know is whether the maximum count exceeds the historical maximum count, and that can only happen because of the newly added char.
            max_repeat_letter_count = max(max_repeat_letter_count, letter_frequency[curr_letter])

            # Basically after the first time we add set our max_len, if the max_repeat_letter_count doesn't increase then we will just shift our window until the max_repeat_letter_count does increase (i.e., we have a window where we have to make fewer replacements).  Only once our max_repeat_letter_count increases again will our window be allowed to expand rather than just shifting
            if (end - start + 1 - max_repeat_letter_count > k):
                start_char = str1[start]
                letter_frequency[start_char] -= 1
                start += 1
            #check if our current window size (which should be valid with regards to k after our shift) is the max_len
            max_len = max(max_len, end - start + 1)

        return max_len


def main():
    sol = Solution()
    print(sol.longest_after_replacement("aabccbb", 2))
    print(sol.longest_after_replacement("abbcb", 1))
    print(sol.longest_after_replacement("abccde", 1))
    print(sol.longest_after_replacement("aaaabccdaaaeeaaaaaaa", 2))
  

main()