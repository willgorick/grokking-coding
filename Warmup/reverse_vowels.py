"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

from collections import deque

class Solution:
  def reverse_vowels(self, x):
    stack = deque()
    vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    str_list = [letter for letter in x]

    for i in range(len(str_list)):
      if str_list[i] in vowel_set:
        stack.append(x[i])
        str_list[i] = "*"

    for i in range(len(str_list)):
      if str_list[i] == "*":
        replacement = stack.pop()
        str_list[i] = replacement
    return "".join(str_list)

def main():
  sol = Solution()
  assert(sol.reverse_vowels("DesignGUrus") == "DusUgnGires")
  assert(sol.reverse_vowels("AEIOU") == "UOIEA")
  assert(sol.reverse_vowels("hello") == "holle")
  

if __name__ == "__main__":
  main()