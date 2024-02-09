"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string.

Time Complexity: O(N+M) - where N is the length of the string and M is the length of the pattern (loop through pattern to get frequencies, loop through the string to check for the permutations)
Space Complexity: O(M) - if all distinct letters in the pattern then the hashmap will be length M

"""

class Solution:
  def findPermutation(self, str1, pattern):
    pattern_len = len(pattern)
    start, matched = 0, 0
    pattern_freq = {}

    #get the frequency of each character in the pattern
    for letter in pattern:
      if letter not in pattern_freq:
        pattern_freq[letter] = 0 
      pattern_freq[letter] += 1
        

    for end in range(len(str1)):
      curr_letter = str1[end]
      #decrement the frequency of the character 
      if curr_letter in pattern_freq:
        pattern_freq[curr_letter] -= 1
        #if the character goes down to zero, increase our matched count
        if pattern_freq[curr_letter] == 0:
          matched += 1

      #if we've successfully matched every character, return true
      if matched == len(pattern_freq):
        return True

      #once we've reached out pattern length, shift the window every time
      if end >= pattern_len-1:
        start_letter = str1[start]
        if start_letter in pattern_freq:
          #if we previously matched the letter moving out of the window, decrement our matched count
          if pattern_freq[start_letter] == 0:
            matched -= 1
          #add the letter back to the pattern freq
          pattern_freq[start_letter] += 1
        start += 1

    return False


def main():
  sol = Solution()
  print('Permutation exist: ' + str(sol.findPermutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(sol.findPermutation("odicf", "dc")))
  print('Permutation exist: ' + str(sol.findPermutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(sol.findPermutation("aaacb", "abc")))
  

main()