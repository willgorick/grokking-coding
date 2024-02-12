"""
We are given an array containing n numbers, all between 1 and n with no duplicates.
Write a function to sort the numbers in-place in O(n) and without using any extra space. 

Time Complexity: O(n) - we will look at each number a maximum of two times (if we got the wrong number at index 0 every time then we would perform n-1 swaps, then when looking at each other index we would continue without swapping).
Space Complexity: O(1)

"""

class Solution:
    def cyclic_sort(self, nums):
        i = 0
        while i < len(nums):
            proper_index = nums[i] -1
            if nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1
        return nums


def main():
    sol = Solution()
    print(sol.cyclic_sort([3, 1, 5, 4, 2]))
    print(sol.cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(sol.cyclic_sort([1, 5, 6, 4, 3, 2]))
  

main()

