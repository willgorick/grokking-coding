"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from collections import defaultdict

class Solution:
  def valid_anagram(self, s, t):
    letter_count = defaultdict(int)
    for letter in s:
      letter_count[letter] += 1
    for letter in t:
      letter_count[letter] -= 1
    for letter in letter_count:
      if letter_count[letter] != 0:
          return False
  
    return True


def main():
  sol = Solution()
  assert(sol.valid_anagram("listen", "silent") == True)
  assert(sol.valid_anagram("a", "b") == False)
  

if __name__ == "__main__":
  main()