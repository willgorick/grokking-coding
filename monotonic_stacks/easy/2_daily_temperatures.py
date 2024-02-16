"""
Given an array of integers temperatures representing daily temperatures, your task is to calculate how many days you have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Time Complexity: O(n) for loop is linear and each value is popped from the stack at most once
Space Complexity: O(n) size of the stack as well as the result array
"""


class Solution:
    def daily_temperatures(self, temps):
        stack = []
        result = [0]*len(temps)

        for i in range(len(temps)):
            # the reason we can pop the idx value from the stack is that we find the closest greater temperature via the order of this for loop, so once we've set a value in the result array it's guaranteed to be the closest and we can get that value out of our stack
            # ex: [74, 73, 72, 71, 75]
            # each loop we never set thee result value because each temps[i] is less than the values before it, except for the 75.  When we get to 75's index the while loop will set the closest greater temp via the while loop for each value that came before it
            while stack and temps[i] > temps[stack[-1]]:
                idx = stack.pop()
                result[idx] = i-idx
            # push current index onto stack
            stack.append(i)
        return result


def main():
    sol = Solution()
    print(sol.daily_temperatures([70, 73, 75, 71, 69, 72, 76, 73]))
    print(sol.daily_temperatures([73, 72, 71, 70]))
    print(sol.daily_temperatures([70, 71, 72, 73]))
    print(sol.daily_temperatures([74, 73, 72, 71, 75]))


main()
