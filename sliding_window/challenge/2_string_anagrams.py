"""
Given a string and a pattern, find and return the indices of all anagrams of the pattern in the given string.

Time Complexity: O(N+M) - see permutation in a string (same problem just returning the indices rather than true/false)
Space Complexity: O(M)

"""


class Solution:
    def string_anagrams(self, str1, pattern):
        result = []
        pattern_len = len(pattern)
        start, matched = 0, 0
        pattern_freq = {}
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

            if matched == len(pattern_freq):
                result.append(start)

            if end >= pattern_len-1:
                start_letter = str1[start]
                if start_letter in pattern_freq:
                    if pattern_freq[start_letter] == 0:
                        matched -= 1
                    pattern_freq[start_letter] += 1
                start += 1
        return result


def main():
    sol = Solution()
    print(sol.string_anagrams("ppqp", "pq"))
    print(sol.string_anagrams("abbcabc", "abc"))
    print(sol.string_anagrams("hellothere", "there"))


main()
