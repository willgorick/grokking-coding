"""
Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
"""

class Solution:
  def word_distance(self, words, word1, word2):
    word_distance = len(words)
    word1_index, word2_index = -1, -1

    for i in range(len(words)):
      if words[i] == word1:
        word1_index = i
      elif words[i] == word2:
        word2_index = i
      
      if word1_index != -1 and word2_index != -1:
        word_distance = min(word_distance, abs(word1_index - word2_index))
    return word_distance
  
def main():
  sol = Solution()
  assert(sol.word_distance(["a", "c", "d", "b", "a"], "a", "b") == 1)
  assert(sol.word_distance(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], "fox", "dog") == 5)
  

if __name__ == "__main__":
  main()