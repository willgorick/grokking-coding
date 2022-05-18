def non_repeat_substring(str):
	start_ind, max_len = 0, 0
	char_ind_map = {}
	for end_ind in range(len(str)):
		next_char = str[end_ind]
		if next_char in char_ind_map:
			# if we've already seen this character, we want to move the window if the previous index of that character (+1) is greater than our current window start
			start_ind = max(start_ind, char_ind_map[next_char]+1)
		char_ind_map[next_char] = end_ind
		max_len = max(max_len, end_ind - start_ind +1)
	return max_len

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()