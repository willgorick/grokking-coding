

def solve_knapsack(profits, weights, cap):
  # return brute_recursive(profits, weights, cap, 0)
  # dp = [[-1 for x in range(cap+1)] for y in range(len(profits))]
  # return top_down_memoization(dp, profits, weights, cap, 0)
  # return bottom_up_dp(profits, weights, cap)
  return optimized_dp(profits, weights, cap)

def brute_recursive(profits, weights, cap, ind): #at each step, find the max profit from subset with and without the current item
  if cap <= 0 or ind >= len(profits): #reached all the items or run out of capacity
    return 0

  profit1 = 0
  if weights[ind] <= cap:
    profit1 = profits[ind] + brute_recursive(profits, weights, cap-weights[ind], ind+1)
  profit2 = brute_recursive(profits, weights, cap, ind+1)

  return max(profit1, profit2)

def top_down_memoization(dp, profits, weights, cap, ind): 
  if cap <=0 or ind >= len(profits):
    return 0
  if dp[ind][cap] != -1:
    return dp[ind][cap]

  profit1 = 0
  if weights[ind] <= cap:
    profit1 = profits[ind] + brute_recursive(profits, weights, cap-weights[ind], ind+1)
  profit2 = brute_recursive(profits, weights, cap, ind+1)

  dp[ind][cap] = max(profit1, profit2)

  return dp[ind][cap]

def bottom_up_dp(profits, weights, cap):
  n = len(profits)
  if cap <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(cap+1)] for y in range(n)]

  #any column with 0 capacity will have 0 profit
  for i in range(0, n):
    dp[i][0] = 0

  for c in range(0, cap+1):
    if weights[0] <= c: #if first element weight is less than available cap always add it
      dp[0][c] = profits[0]

  for i in range(1, n):
    for c in range(1, cap+1):
      profit1, profit2 = 0, 0
      if weights[i] <= c: #we can add
        profit1 = profits[i] + dp[i-1][c-weights[i]] # add profit for this item + profit of the previous item at the capacity - weight of this item
      profit2 = dp[i-1][c] #profit2 is profit from the previous item
      dp[i][c] = max(profit1, profit2)
  
  print_selected_elements(dp, weights, profits, cap)
  return dp[n-1][cap]

def optimized_dp(profits, weights, cap):
  # basic checks
  n = len(profits)
  if cap <= 0 or n == 0 or len(weights) != n:
    return 0

  # we only need one previous row to find the optimal solution, overall we need '2' rows
  # this solution is similar to the previous solution, the only difference is that
  # we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`
  dp = [[0 for x in range(cap+1)] for y in range(2)]

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, cap+1):
    if weights[0] <= c:
      dp[0][c] = dp[1][c] = profits[0]

  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(0, cap+1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
      # exclude the item
      profit2 = dp[(i - 1) % 2][c]
      # take maximum
      dp[i % 2][c] = max(profit1, profit2)

  return dp[(n - 1) % 2][cap]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

def print_selected_elements(dp, weights, profits, cap):
  print("Selected weights are: ", end="")
  n = len(weights)
  total_prof = dp[n-1][cap]
  for i in range(n-1, 0, -1): #for each weight
    if total_prof != dp[i-1][cap]: #if the profit at a given spot is higher than before we evaluated this item, that means this item was added to our knapsack
      print(str(weights[i]) + " ", end="")
      cap -= weights[i] #decrease our cap by weight of this element so we look at that column now
      total_prof -= profits[i]

  if total_prof != 0: #if we get to the end and still have profit left, we must've added the first element (we can't do i-1 of 0, that's why we need this case outside the loop)
    print(str(weights[0]) + " ", end="")
  print()

main()

