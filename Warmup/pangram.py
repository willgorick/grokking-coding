"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or false otherwise.

Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.
"""

class Solution:
  def pangram(self, sentence):
    letter_set = set()
    for letter in sentence.lower():
      if letter.isalpha() and letter not in letter_set:
        letter_set.add(letter)

    return len(letter_set) == 26


def main():
  sol = Solution()
  assert(sol.pangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == True)
  assert(sol.pangram("TheQuickBrownFoxJumpsOverTheLazyDog") == True)
  assert(sol.pangram("This is not a pangram") == False)

if __name__ == "__main__":
  main()