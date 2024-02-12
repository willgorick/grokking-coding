"""
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Time Complexity: O(n+k), as if we had [1,2,3,4] we would loop through this initially and then need our result to consist of the next k numbers after 4
Space Complexity: O(k) as we only add numbers to the extra set if they are out of order and we haven't decreased k to zero, meaning we will only add up to k numbers
"""

class Solution:
    def first_k_missing_positive_numbers(self, nums, k):
        i = 0
        extra_nums_set = set()

        #regular cyclic sort, just with additional bounds checking
        while i < len(nums):
            proper_index = nums[i] -1
            if proper_index >= 0 and proper_index < len(nums) and nums[i] != nums[proper_index]:
                nums[i], nums[proper_index] = nums[proper_index], nums[i]
            else:
                i += 1

        result = []
        for i in range(len(nums)):
            #if we already have k numbers in our result, break
            if k == 0:
                break
            #if we find a missing number, add it to the result, decrement k, and put the number that was in its place in our extra_nums set
            if i != nums[i]-1:
                result.append(i+1)
                k -= 1
                extra_nums_set.add(nums[i])

        #until we've reached k numbers, starting from the len of the array +1, check if each number has is in our extra_nums_set, and add it to the result if it wasn't
        potential_next_positive = len(nums)+1
        while k > 0:
            if potential_next_positive not in extra_nums_set:
                result.append(potential_next_positive)
                k -= 1
            potential_next_positive += 1
        return result

            


def main():
    sol = Solution()
    print(sol.first_k_missing_positive_numbers([3, -1, 4, 5, 5], 3))
    print(sol.first_k_missing_positive_numbers([2, 3, 4], 3))
    print(sol.first_k_missing_positive_numbers([-2, -3, 4], 2))
    print(sol.first_k_missing_positive_numbers([1, 3, 4], 2))
    print(sol.first_k_missing_positive_numbers([5, 6, 7, 8], 5))

  

main()