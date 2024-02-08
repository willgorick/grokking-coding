"""
Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

Time Complexity: O(n) we consider each element as the last element in our subarray exactly once
Space Complexity: O(1) we store two pointers and two sums (the current and the max)

"""

class Solution:
  def max_sum_of_subarray(self, k, arr):
    start, curr_sum, max_sum = 0, 0, 0

    for end in range(len(arr)):
      curr_sum += arr[end]
      if end >= k-1:
        max_sum = max(curr_sum, max_sum)
        curr_sum -= arr[start]
        start += 1
    return max_sum


def main():
  sol = Solution()
  print("Maximum sum of a subarray of size K: " +
        str(sol.max_sum_of_subarray(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " +
        str(sol.max_sum_of_subarray(2, [2, 3, 4, 1, 5])))
  

main()