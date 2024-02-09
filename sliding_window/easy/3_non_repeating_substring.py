"""
Given a string s, find the length of the longest 
substring without repeating characters.
 
Time Complexity:
Space Complexity:
"""

def non_repeat_substring(str):
	start, max_len = 0, 0
	char_ind_map = {}
	for end in range(len(str)):
		next_char = str[end]
		if next_char in char_ind_map:
			# if we've already seen this character, we want to move the window if the previous index of that character (+1) is greater than our current window start
			start = max(start, char_ind_map[next_char]+1)
		#update our index for this character
		char_ind_map[next_char] = end
		#update our max if our current window is larger
		max_len = max(max_len, end - start +1)
	return max_len

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()