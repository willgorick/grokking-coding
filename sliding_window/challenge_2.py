
def string_anagrams(string, pattern):
  char_freq = {}
  for letter in pattern:
    if letter not in char_freq:
      char_freq[letter] = 0
    char_freq[letter] += 1

  start, matched_chars = 0,0
  res = []
  for i in range(len(string)):
    end_char = string[i]
    if end_char in char_freq:
      char_freq[end_char] -= 1
      if char_freq[end_char] == 0:
        matched_chars += 1
    if matched_chars == len(char_freq):
      res.append(start)

    if i >= len(pattern)-1:
      remove = string[start]
      start += 1
      if remove in char_freq:
        if char_freq[remove] == 0:
          matched_chars -= 1
        char_freq[remove] += 1
  return res

def main():
  print(string_anagrams("ppqp", "pq"))
  print(string_anagrams("abbcabc", "abc"))

main()