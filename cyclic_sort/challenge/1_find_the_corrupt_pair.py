"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Time Complexity: O(n) - 2n for while loop, n for for loop
Space Complexity: O(1)

"""


class Solution:
    def find_the_corrupt_pair(self, nums):
        i = 0
        while i < len(nums):
            proper_index = nums[i]-1
            if nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return [nums[i], i+1]
        return [-1, -1]


def main():
    sol = Solution()
    print(sol.find_the_corrupt_pair([3, 1, 2, 5, 2]))
    print(sol.find_the_corrupt_pair([3, 1, 2, 3, 6, 4]))


main()
