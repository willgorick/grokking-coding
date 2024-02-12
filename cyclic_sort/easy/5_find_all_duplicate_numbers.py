"""
We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers appearing twice, find all these duplicate numbers using constant space.

Time Complexity: O(n) - 2n for the while loop, n for the for loop
Space Complexity: O(n) for the result array

"""


class Solution:
    def find_all_duplicate_numbers(self, nums):
        i = 0
        # just cyclic sort and then check for the number out of place
        while i < len(nums):
            proper_index = nums[i]-1
            if nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1
        duplicates = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                duplicates.append(nums[i])
        return duplicates


def main():
    sol = Solution()
    print(sol.find_all_duplicate_numbers([3, 4, 4, 5, 5]))
    print(sol.find_all_duplicate_numbers([5, 4, 7, 2, 3, 5, 3]))


main()
