"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.
Note: Positive numbers start from '1'.

Time Complexity: O(n) - 2n for the while loop, n for the for loop
Space Complexity: O(1)

"""


class Solution:
    def smallest_missing_positive_number(self, nums):
        i = 0
        # cyclic sort and then check for a number out of place
        while i < len(nums):
            proper_index = nums[i]-1
            # have to check if the "proper_index" is in bounds of the array
            if proper_index >= 0 and proper_index < len(nums) and nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if i != nums[i]-1:
                return i+1
        # basically if no number is missing then return the next positive number
        return len(nums)+1


def main():
    sol = Solution()
    print(sol.smallest_missing_positive_number([-3, 1, 5, 4, 2]))
    print(sol.smallest_missing_positive_number([3, -2, 0, 1, 2]))
    print(sol.smallest_missing_positive_number([3, 2, 5, 1]))
    print(sol.smallest_missing_positive_number([33, 37, 5]))


main()
