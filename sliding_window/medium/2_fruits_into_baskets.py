"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Time Complexity: O(n) this is just longest substring with k distinct characters where k = 2
Space Complexity: O(k)

"""

from collections import defaultdict


class Solution:
    def fruit_into_baskets(self, fruits):
        max_length = 0
        baskets = defaultdict(int)
        start = 0

        for end in range(len(fruits)):
            curr_fruit = fruits[end]
            baskets[curr_fruit] += 1
            if len(baskets) <= 2:
                max_length = max(max_length, end-start+1)
            while len(baskets) > 2:
                start_fruit = fruits[start]
                baskets[start_fruit] -= 1
                if baskets[start_fruit] == 0:
                    del baskets[start_fruit]
                start += 1

        return max_length


def main():
    sol = Solution()
    print("Maximum number of fruits: "
          + str(sol.fruit_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: "
          + str(sol.fruit_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
