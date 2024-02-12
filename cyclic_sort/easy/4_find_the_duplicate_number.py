"""
We are given an unsorted array containing n+1 numbers taken from the range 1 to n. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Time Complexity: O(n) - 2n for the while loop, n for the for loop
Space Complexity: O(1)

"""


class Solution:
    def find_the_duplicate_number(self, nums):
        i = 0
        # just cyclic sort and then check for the number out of place
        while i < len(nums):
            proper_index = nums[i]-1
            if nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]
        return -1


def main():
    sol = Solution()
    print(sol.find_the_duplicate_number([1, 4, 4, 3, 2]))
    print(sol.find_the_duplicate_number([2, 1, 3, 3, 5, 4]))
    print(sol.find_the_duplicate_number([2, 4, 1, 4, 4]))


main()
