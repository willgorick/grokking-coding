"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Time Complexity: O(n) same as longest substring after replacement
Space Complexity: O(1) - just a few maximum values and the two pointers

"""
from collections import defaultdict


class Solution:
    def most_ones_after_replacement(self, arr, k):
        start, max_len, max_ones_count = 0, 0, 0

        for end in range(len(arr)):
            curr_number = arr[end]
            max_ones_count += 1 if curr_number == 1 else 0

            if (end-start+1 - max_ones_count > k):
                start_num = arr[start]
                max_ones_count -= 1 if start_num == 1 else 0
                start += 1
            max_len = max(end-start+1, max_len)

        return max_len


def main():
    sol = Solution()
    print(sol.most_ones_after_replacement(
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(sol.most_ones_after_replacement(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
