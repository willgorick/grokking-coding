"""
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Time Complexity: O(N+M) same as permutations (all letters in pattern, all letters in string)
Space Complexity: O(N) in the case where we require all letters from the string to complete the pattern (i.e., "azzzzzzzbzzzzzzc", "abc")

"""

class Solution:
  def smallest_window_containing_substring(self, str1, pattern):
    start, matched = 0, 0
    smallest_window_size = float("inf")
    smallest_window_found = ""
    pattern_freq = {}

    #same as string permutations initially, add characters and decrement their frequency if they're in the pattern
    for letter in pattern:
      if letter not in pattern_freq:
        pattern_freq[letter] = 0
      pattern_freq[letter] += 1
    
    for end in range(len(str1)):
      curr_letter = str1[end]
      if curr_letter in pattern_freq:
        pattern_freq[curr_letter] -= 1
        if pattern_freq[curr_letter] == 0:
          matched += 1
      
      #differentiates from permutations here: once we have all the characters we attempt to shrink our window as much as possible until we no longer have matches for all characters in the pattern
      while matched == len(pattern_freq):
        if end-start+1 < smallest_window_size:
          smallest_window_size = end-start+1
          smallest_window_found = str1[start:end+1]
        start_letter = str1[start]
        if start_letter in pattern_freq:
          if pattern_freq[start_letter] == 0:
            matched -= 1
          pattern_freq[start_letter] += 1
        start += 1

    return smallest_window_found
    


def main():
  sol = Solution()
  print(sol.smallest_window_containing_substring("aabdec", "abc"))
  print(sol.smallest_window_containing_substring("aabdec", "abac"))
  print(sol.smallest_window_containing_substring("abdbca", "abc"))
  print(sol.smallest_window_containing_substring("adcad", "abc"))
  print(sol.smallest_window_containing_substring("azzzzzzzbzzzzzzc", "abc"))
  

main()