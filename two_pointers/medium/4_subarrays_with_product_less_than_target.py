"""
Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

Time Complexity: O(n^3), O(n) for the main sliding window + O(n^2) for creating the subarrays in the worst case so O(n^3)
Space Complexity: O(n^3), O(n) space for each subarray and O(n^2) subarrays in the worst case
"""
from collections import deque


class Solution:
    def subarrays_with_smaller_product(self, arr, target):
        result = []
        product = 1
        left = 0
        for right in range(len(arr)):
            product *= arr[right]

            # If we ever get over the product, divide out the leftmost digit and move the left pointer to the right
            while product >= target and left < len(arr):
                product /= arr[left]
                left += 1

            # Create a temporary list to store the current subarray.
            temp_list = deque()

            # For each element between right and left, add a list with the first one, then two, etc.
            for i in range(right, left-1, -1):
                temp_list.appendleft(arr[i])
                result.append(list(temp_list))
        return result


def main():
    sol = Solution()
    print(sol.subarrays_with_smaller_product([2, 5, 3, 10], 30))
    print(sol.subarrays_with_smaller_product([8, 2, 6, 5], 50))


main()
