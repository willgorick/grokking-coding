def contains_permutation(str, pattern):
    start_ind, matched_chars = 0, 0
    char_freq = {}
    for char in pattern:
      if char not in char_freq:
        char_freq[char] = 0
      char_freq[char] += 1
    for end_ind in range(len(str)):
      curr_char = str[end_ind]
      if curr_char in char_freq:
        char_freq[curr_char] -= 1
        if char_freq[curr_char] == 0:
          matched_chars += 1
      if matched_chars == len(char_freq):
        return True
      if end_ind >= len(pattern) - 1:
        remove = str[start_ind]
        start_ind += 1
        if remove in char_freq:
          if char_freq[remove] == 0:
            matched_chars -=1
          char_freq[remove] += 1
    return False

def main():
  print('Permutation exist: ' + str(contains_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(contains_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(contains_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(contains_permutation("aaacb", "abc")))


main()