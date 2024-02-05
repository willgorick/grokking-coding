"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Time Complexity: O(n^2), sort is O(n log n), but this is less than O(n^2) from outer loop plus linear worst case for inner loop (either right decreases or left increases each iteration)
Space Complexity: O(n) for sort
"""


"""
Similar problem (return_all_triplets_with_smaller_sum)
Write a function to return the list of all such triplets instead of the count. How will the time complexity change in this case?

Time Complexity: O(n^3) because in the worst case scenario all triplets in the array will be smaller than the target sum, so the nested for loop inside the while could be O(n)
"""
class Solution:
  def triplets_with_smaller_sum(self, arr, target):
    count = 0
    arr.sort()
    for i in range(len(arr)-2): #-2 because the last triplet we want to consider is the final 3 numbers
      curr = arr[i]
      left, right = i+1, len(arr)-1
      while left < right:
        if curr + arr[left] + arr[right] < target:
          count += right - left #because arr[right] > arr[left], all numbers between will also be less than the sum (i.e, for 0, 1, 4 we can assume 0,1,3 and 0,1,2 are also less than target)
          left += 1
        #if we're >= target then shift the right pointer to make the current sum smaller
        else:
          right -= 1
    return count

  def return_all_triplets_with_smaller_sum(self, arr, target):
    triplets = []
    arr.sort()
    for i in range(len(arr)-2): #-2 because the last triplet we want to consider is the final 3 numbers
      curr = arr[i]
      left, right = i+1, len(arr)-1
      while left < right:
        if curr + arr[left] + arr[right] < target:
          for i in range(right, left, -1):
            triplets.append([curr, arr[left], arr[i]])
          left += 1
        else:
          right -= 1
    return triplets

def main():
  sol = Solution()
  print(sol.triplets_with_smaller_sum([-1, 0, 2, 3], 3))
  print(sol.triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))

  print(sol.return_all_triplets_with_smaller_sum([-1, 0, 2, 3], 3))
  print(sol.return_all_triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))

main()