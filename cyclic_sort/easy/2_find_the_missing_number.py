"""
We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Time Complexity: O(n), while loop will repeat at most 2n times (cyclic sort), then we have one more linear loop to find the missing value
Space Complexity: O(1)
"""


class Solution:
    def find_missing_number(self, nums):
        i, n = 0, len(nums)
        # because this is from 0 to n, we compare the value to its index directly rather than the number -1 (which we previously did in cyclic sort to zero index our numbers)
        while i < n:
            proper_index = nums[i]
            # because the indices are 0 to n-1 and the numbers are 0 to n we have to check if our proper_index value is out of bounds (if so don't try to move it)
            if proper_index < n and nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1
        # the first index we find where the wrong number is in place is the missing number
        # i.e., [3, 2, 4, 0, 5]  -> [0, 2, 3, 4, 5] - at index 1 we see 2, meaning 1 is the missing number
        for i in range(n):
            if nums[i] != i:
                return i

        # if we didn't find a value out of place that means that the missing number is n (which doesn't have a proper index)
        # i.e., [5, 4, 2, 1, 0, 3] -> [0, 1, 2, 3, 4, 5] -> 6 is missing
        return n


def main():
    sol = Solution()
    print(sol.find_missing_number([4, 0, 3, 1]))
    print(sol.find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
    print(sol.find_missing_number([7, 3, 5, 2, 4, 6, 0, 1]))
    print(sol.find_missing_number([3, 2, 5, 4, 1]))


main()
