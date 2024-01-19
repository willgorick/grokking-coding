"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Time Complexity: O(n^2) - 
  Loop through the array (O(n)) and perform a linear two pointer scan each time (also O(n)) => O(n^2)
Space Complexity: O(n) for sorting
"""

import math

class Solution:
  def triplet_sum_close_to_target(self, arr, target_sum):
    arr.sort()
    closest_distance = float("inf")
    closest_sum = float("inf")
    arr_len = len(arr)   

    for i in range(arr_len-1):
      # skip duplicates
      if i > 0 and arr[i] == arr[i]-1:
        continue

      l, r= i+1, arr_len-1
      while l < r:
        triple_sum = arr[l] + arr[r] + arr[i]
        diff = target_sum - triple_sum
        if diff == 0:
          return target_sum
        
        # or checks if this current sum is smaller than the previously evaluated triplet that is the same distance away from the target
        if abs(diff) < abs(closest_distance) or (abs(diff) == abs(closest_distance) and triple_sum < closest_sum):
          closest_distance = diff
          closest_sum = triple_sum

        # we want our triple_sum to be larger to be closer to the target_sum
        elif diff > 0:
          l += 1

        # we want our triple to be smaller because it is currently larger than the target_sum
        else:
          r -= 1
    return target_sum - closest_distance

def main():
  sol = Solution()
  print(sol.triplet_sum_close_to_target([-1, 0, 2, 3], 3))
  print(sol.triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(sol.triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(sol.triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()