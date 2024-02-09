"""
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Time Complexity: O(N*M): where N is the length of str1, M is the number of words, and Len is the length of the words.  N for the outer loop, M for the inner loop, and Len for slicing the word chunks from the string
Space Complexity: O(M+N) - O(N) potentially for result list, O(M) for both word_freq and the words_seen lists

"""

class Solution:
  def find_word_concat(self, str1, words):
    word_count = len(words)
    word_len = len(words[0])
    result = []
    #if no words or words are empty strings just return []
    if word_count == 0 or word_len == 0:
      return result
    
    word_freq = {}
    for word in words:
      if word not in word_freq:
        word_freq[word] = 0
      word_freq[word] += 1

    #this loop ensures we start at all valid starting indices (basically any index where there are word_count*word_len remaining characters).  Any index after this would not have enough space to include all the words we are matching to
    for i in range((len(str1) - (word_count * word_len))+1):
      #re-initialize our words_seen dict for each starting index
      words_seen = {}
      #loop through word_count times to make sure we find each word from the list
      for j in range(word_count):
        #i index + length of a word to look for the next word
        next_word_index = i + (j*word_len)
        word = str1[next_word_index: next_word_index+word_len]

        #not a valid word, so break
        if word not in word_freq:
          break

        #update the number of times we've seen this word from this starting index
        if word not in words_seen:
          words_seen[word] = 0
        words_seen[word] += 1
          
        #we've seen this word too many times so break
        if words_seen[word] > word_freq.get(word, 0):
          break

        #if we've made it to the end fo the loop without breaking, then we've found all the words, so add the starting ind to our result
        if j + 1 == word_count:
          result.append(i)
    return result


    
    
    


def main():
  sol = Solution()
  print(sol.find_word_concat("catfoxcat", ["cat", "fox"]))
  print(sol.find_word_concat("catcatfoxfox", ["cat", "fox"]))
  

main()