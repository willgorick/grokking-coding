"""
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

"""
from collections import deque

class Solution:
  def subarrays_with_smaller_product(self, arr, target):
      result = []
      product = 1
      left = 0
      for right in range(len(arr)):
          product *= arr[right]

          #If we ever get over the product, divide out the leftmost digit and move the left pointer to the right
          while product >= target and left < len(arr):
              product /= arr[left]
              left += 1

          # Create a temporary list to store the current subarray.
          temp_list = deque()

          # For each element between right and left, add a list with the first one, then two, etc.
          for i in range(right, left-1, -1):
              temp_list.appendleft(arr[i])
              result.append(list(temp_list))
      return result

sol = Solution()
print(sol.subarrays_with_smaller_product([2, 5, 3, 10], 30))
print(sol.subarrays_with_smaller_product([8, 2, 6, 5], 50))
