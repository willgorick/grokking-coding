"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
You can assume that K is less than or equal to the length of the given string.

Time Complexity: O(n) - The outer for loop looks at each character once, and the inner while loop looks at each character at most once
Space Complexity: O(k) for storing k+1 characters in our defaultdict at most

"""
from collections import defaultdict

class Solution:
  def longest_substring(self, str1, k):
    max_length, start = 0, 0
    curr_letters = defaultdict(int)

    for end in range(len(str1)):
      curr_letters[str1[end]] += 1
      if len(curr_letters) <= k:
        max_length = max(max_length, end-start+1)

      #while too many letters, keep advancing the start pointer forward until one of our letter counts goes to zero
      while len(curr_letters) > k:
        start_letter = str1[start]
        curr_letters[start_letter] -= 1
        if curr_letters[start_letter] == 0:
          del curr_letters[start_letter]
        start += 1
      
    return max_length



def main():
  sol = Solution()
  print(sol.longest_substring("araaci", 2))
  print(sol.longest_substring("araaci", 1))
  print(sol.longest_substring("cbbebi", 3))
  

main()