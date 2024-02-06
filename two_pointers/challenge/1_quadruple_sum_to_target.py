"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.


Time Complexity: O(n^3), sorting takes O(n log n), but the nested for loops take O(n^2) and then the actual sliding window (search_pairs) is O(n) each time resulting in O(n^3)
Space Complexity: O(n) for sorting (and theoretically O(n-3) possible answers for the output)

"""

class Solution:
  def quadruple_sum_to_target(self, arr, target):
    arr.sort()
    quadruplets = []

    def search_pairs(quadruplets, val_i, val_j, left, right):
      while left < right:
        val_left, val_right = arr[left], arr[right]
        curr_sum = val_i + val_j + val_left + val_right
        if curr_sum == target:
          quadruplets.append([val_i, val_j, val_left, val_right])
          left += 1
          right -= 1
          while left < len(arr) and arr[left] == arr[left-1]:
            left += 1
          while right >= 0 and arr[right] == arr[right+1]:
            right -= 1
        elif curr_sum < target:
          left += 1
        else:
          right -= 1
          
    # Nested for loop to get each combination of two numbers as our i and j
    for i in range(0, len(arr)-4):
      if i > 0 and arr[i] == arr[i-1]:
        continue

      for j in range(i+1, len(arr)-3):
        if arr[j] == arr[j-1]:
          continue
        # left and right are chosen from the remaining numbers (j +1) and the final value in the array
        left, right = j+1, len(arr)-1
        val_i, val_j = arr[i], arr[j]
        # search pairs functions the exact same as target sum, just with two additional numbers being added to get the sum
        search_pairs(quadruplets, val_i, val_j, left, right)
        
    return quadruplets


def main():
  sol = Solution()
  print(sol.quadruple_sum_to_target([4, 1, 2, -1, 1, -3], 1))
  print(sol.quadruple_sum_to_target([2, 0, -1, 1, -2, 2], 2))
  print(sol.quadruple_sum_to_target([2, 0, -1, 1, -2, 2], 0))
main()