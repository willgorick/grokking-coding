
"""
Given an array of numbers sorted in ascending order and a target sum, find a pair in the array whose sum is equal to the given target. If no such pair exists return [-1, -1].  Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Time Complexity: O(n) (consider each element at most once)
Space Complexity: O(1) (only store two pointers)
"""


class Solution:
    def target_sum(self, arr, target_sum):
        l, r = 0, len(arr)-1

        while l < r:
            curr_sum = arr[l] + arr[r]
            if curr_sum == target_sum:
                return [l, r]
            if curr_sum > target_sum:
                r -= 1
            else:
                l += 1
        return [-1, -1]


def main():
    sol = Solution()
    print(sol.target_sum([1, 2, 3, 4, 6], 6))
    print(sol.target_sum([2, 5, 9, 11], 11))


if __name__ == "__main__":
    main()
