"""
Given an array of integers, identify the highest value that appears only once in the array. If no such number exists, return -1.

Time Complexity: O(n) two loops
Space Complexity: O(n) if all numbers are unique (hash map size)
"""


class Solution:
    def largest_unique(self, nums):
        nums_count = {}

        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        max_unique_value = -1
        for num in nums_count:
            if nums_count[num] == 1 and num > max_unique_value:
                max_unique_value = num
        return max_unique_value


def main():
    sol = Solution()
    print(sol.largest_unique([5, 7, 3, 7, 5, 8]))
    print(sol.largest_unique([1, 2, 3, 2, 1, 4, 4]))
    print(sol.largest_unique([9, 9, 8, 8, 7, 7]))


main()
