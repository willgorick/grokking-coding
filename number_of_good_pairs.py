"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from collections import defaultdict
class Solution:
  def number_of_good_pairs(self, nums):
    number_pairs = 0
    number_map = defaultdict(int)
    for num in nums:
      number_pairs += number_map[num]
      number_map[num] += 1

    return number_pairs

def main():
  sol = Solution()
  assert(sol.number_of_good_pairs([1,2,3,1,1,3]) == 4)
  assert(sol.number_of_good_pairs([1,1,1,1]) == 6)
  

if __name__ == "__main__":
  main()