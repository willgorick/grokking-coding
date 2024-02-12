"""
Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place. The relative order of the elements should be kept the same and you should not use any extra space so that the solution has constant space complexity i.e., O(1).

Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Time Complexity: O(n) - every iteration through the loop we look at the next value
Space Complexity: O(1) - only two pointers needed
"""


class Solution:
    def remove_duplicates(self, arr):
        # index of the next non-duplicate element
        # start at 1 because idx 0 is where the first non-duplicate will be
        next_non_duplicate = 1

        potential_next_number = 0
        while (potential_next_number < len(arr)):
            # check if current number is equal to the last non-duplicate we found
            # next_non_duplicate - 1 is the last non-duplicate we found
            # if it is not equal, then we've found a new non-duplicate, and we should put it at the next_non_duplicate index and increment that index
            last_non_duplicate_number = next_non_duplicate-1
            if arr[last_non_duplicate_number] != arr[potential_next_number]:
                arr[next_non_duplicate] = arr[potential_next_number]
                next_non_duplicate += 1
            # regardless of if we found a non-duplicate, we should increment the current index we're looking at
            potential_next_number += 1
        return next_non_duplicate


def main():
    sol = Solution()
    print(sol.remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(sol.remove_duplicates([2, 2, 2, 11]))
    print(sol.remove_duplicates([1, 1, 1, 1, 1]))


if __name__ == "__main__":
    main()
