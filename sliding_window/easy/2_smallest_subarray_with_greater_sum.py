"""
Given an array of positive integers and a number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

Time Complexity: O(n) we essentially look at each value in the array at most twice (once with the end pointer and once more if we shrink the array with the start pointer)
Space Complexity: O(1) for pointers, sum, and length

"""


class Solution:
    def smallest_subarray(self, s, arr):
        start, curr_sum, smallest_len = 0, 0, float('inf')

        for end in range(len(arr)):
            # add next value to sum
            curr_sum += arr[end]

            # move the start pointer forward so long as the sum stays >= the specified value and subtract out the value no longer included
            while start <= end and curr_sum >= s:
                smallest_len = min(smallest_len, end-start+1)
                curr_sum -= arr[start]
                start += 1

        if smallest_len == float('inf'):
            return 0
        return smallest_len


def main():
    sol = Solution()
    print("Smallest subarray length: " +
          str(sol.smallest_subarray(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(sol.smallest_subarray(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(sol.smallest_subarray(8, [3, 4, 1, 1, 6])))


main()
