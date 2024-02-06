"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Time Complexity: O(n) basically we perform several linear loops - one each for finding the initial low and high points, then one for finding our subarray max and min, then one each to expand our subarray based on that max/min
Space Complexity: O(1), just pointers and the max/min

"""

class Solution:
  def minimum_window_sort(self, arr):
    l = 0
    r = len(arr)-1
    #find first number out of order from the left
    while l < len(arr)-1 and arr[l] <= arr[l+1]:
      l += 1

    if l == len(arr) - 1:  # the array is sorted
      return 0

    while r > 0 and arr[r] >= arr[r-1]:
      r -= 1
      
    min_subarray, max_subarray = float("inf"), -float("inf")

    for i in range(l, r+1):
      min_subarray = min(min_subarray, arr[i])
      max_subarray = max(max_subarray, arr[i])
    
    # find any values to the left that are greater than the minimum in our subarray and include them in the sorting
    while l > 0 and arr[l-1] > min_subarray:
      l -= 1

    # find any values to the right that are less than the maximum in our subarray and include them in the sorting
    while r < len(arr)-1 and arr[r+1] < max_subarray:
      r += 1

    return r - l + 1



def main():
  sol = Solution()
  print(sol.minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(sol.minimum_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(sol.minimum_window_sort([1, 2, 3]))
  print(sol.minimum_window_sort([3, 2, 1]))

  
  

main()