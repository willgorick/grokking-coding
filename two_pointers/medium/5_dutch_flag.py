"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

Time Complexity: O(n) because for each iteration of the loop either i increases or r decreases
Space Complexity: O(1) because sorting in place

"""

class Solution:
  def dutch_flag(self, arr):
    l, i, r = 0, 0, len(arr)-1
    # We will move all 0's to below the l and all 2's to above the r

    while i <= r:
      # Swap l and i, increment both (so we don't swap the zero we just put in l)
      if arr[i] == 0:
        arr[l], arr[i] = arr[i], arr[l]
        l += 1
        i += 1
      # Only increment i, 1's stay where they are
      elif arr[i] == 1:
        i += 1
      # Only decrement r so we don't remove the 2 we just put at r, but the new I could have anything so we leave it for the next iteration
      else:
        arr[r], arr[i] = arr[i], arr[r]
        r -= 1
      
    return arr

def main():
  sol = Solution()
  print(sol.dutch_flag([1, 0, 2, 1, 0]))
  print(sol.dutch_flag([2, 2, 0, 1, 2, 0]))

main()