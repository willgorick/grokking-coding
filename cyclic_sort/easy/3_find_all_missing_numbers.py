"""
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.


Time Complexity: O(n) 2n for cyclic sort, then n for the loop to check which numbers are out of order
Space Complexity: O(1)

"""

class Solution:
    def find_all_missing_numbers(self, nums):
        i = 0
        while i < len(nums):
            #proper_index is the index where nums[i] should be
            proper_index = nums[i]-1
            #this if statement checks if either the current number is already at its proper index or a duplicate is already at that index
            if nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1
        missing = []
        #if the wrong number is at an index, then that index+1 is a missing number
        #i.e., [1, 1, 3, 3] -> index 1 is not 2, so 2 is missing and index 3 is not 4 so 4 is missing
        for i in range(len(nums)):
            if nums[i] != i+1:
                missing.append(i+1)
        return missing


def main():
    sol = Solution()
    print(sol.find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(sol.find_all_missing_numbers([2, 4, 1, 2]))
    print(sol.find_all_missing_numbers([2, 3, 2, 1]))
  
main()