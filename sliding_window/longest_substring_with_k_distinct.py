def longest_substring_with_k_distinct(str, k):
	letter_map = {}
	start_ind, longest_len = 0, 0
	for end_ind in range(len(str)):
		curr_letter = str[end_ind]
		if curr_letter not in letter_map:
			letter_map[curr_letter] = 0
		letter_map[curr_letter] += 1

		while len(letter_map) > k:
			remove = str[start_ind]
			letter_map[remove] -= 1
			start_ind += 1
			if letter_map[remove] == 0:
				del letter_map[remove]
		longest_len = max(longest_len, end_ind - start_ind +1)
	return longest_len

def main():
  print("Length of the longest substring: " 
           + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " 
           + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " 
           + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()