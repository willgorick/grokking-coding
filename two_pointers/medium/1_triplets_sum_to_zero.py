"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Time Complexity: O(n^2) - 
  Sorting the algorithm is O(n log(n)).  Each time we call target_sum it is O(n), and we call it for each element, meaning the for loop will take O(n^2), therefore that is the time complexity for the overall algorithm
  Space Complexity: O(n) for the result array (as well as for most sorting algorithms)
"""


class Solution:
    def searchTriplets(self, arr):
        arr.sort()
        triplets = []
        arr_len = len(arr)

        def target_sum(target, l, r):
            while l < r:
                curr_sum = arr[l] + arr[r]
                if curr_sum == target:
                    triplets.append([-target, arr[l], arr[r]])
                    l += 1
                    r -= 1
                    # skip duplicate l and r values by checking if the new index holds the same number as the previous index
                    while l < r and arr[l] == arr[l-1]:
                        l += 1
                    while l < r and arr[r] == arr[r+1]:
                        r -= 1
                elif curr_sum > target:
                    r -= 1
                else:
                    l += 1

        for i in range(arr_len):
            # skip duplicate starting numbers
            if i > 0 and arr[i] == arr[i-1]:
                continue
            target_sum(-arr[i], i+1, arr_len-1)

        return triplets


def main():
    sol = Solution()
    print(sol.searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
    print(sol.searchTriplets([-5, 2, -1, -2, 3]))


if __name__ == "__main__":
    main()
