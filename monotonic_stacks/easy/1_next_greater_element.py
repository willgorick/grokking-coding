"""
Given two integer arrays nums1 and nums2, return an array answer such that answer[i] is the next greater number for every nums1[i] in nums2. The next greater element for an element x is the first element to the right of x that is greater than x. If there is no greater number, output -1 for that number.

The numbers in nums1 are all present in nums2 and nums2 is a permutation of nums1.

Time Complexity: O(n) - even though there are two loops, each element is only pushed and popped at most one time, meaning 2n for the max total number of operations
Space Complexity: O(n) - for both the stack and the hashmap
"""


class Solution:
    def next_greater_element(self, nums1, nums2):
        stack = []
        next_greater_map = {}

        for num in nums2:
            # update map if the number on the top of the stack is smaller than our current number
            while stack and stack[-1] < num:
                # the next greater num for the number being popped is updated to the current number we're looking at
                next_greater_map[stack.pop()] = num
            stack.append(num)
        # if no value then set to -1
        return [next_greater_map.get(num, -1) for num in nums1]


def main():
    sol = Solution()
    nums1 = [4, 2, 6]
    nums2 = [6, 2, 4, 5, 3, 7]
    print(sol.next_greater_element(nums1, nums2))
    nums1 = [9, 7, 1]
    nums2 = [1, 7, 9, 5, 4, 3]
    print(sol.next_greater_element(nums1, nums2))
    nums1 = [5, 12, 3]
    nums2 = [12, 3, 5, 4, 10, 15]
    print(sol.next_greater_element(nums1, nums2))


main()
