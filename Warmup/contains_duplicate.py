"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution: 
  def contains_duplicate(self, nums):
    num_set = set()
    for num in nums:
      if num in num_set:
        return True
      num_set.add(num)
    return False
  

def main():
  sol = Solution()
  assert(sol.contains_duplicate([1,2,3,4]) == False)
  assert(sol.contains_duplicate([1,2,3,4, 1]) == True)

if __name__ == "__main__":
  main()