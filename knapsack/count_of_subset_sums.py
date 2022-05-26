def count_subsets(nums, sum):
  # return brute_force(nums, sum, 0)

  # dp = [[-1 for x in range(sum+1)] for y in range(len(nums))]
  # return top_down_memoization(dp, nums, sum, 0)

  # return(bottom_up_dynamic(nums, sum))

  return(bottom_up_1d_array(nums, sum))


def brute_force(nums, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1
  n = len(nums)
  if n == 0 or currentIndex >= n:
    return 0

  # recursive call after selecting the number at the currentIndex
  # if the number at currentIndex exceeds the sum, we shouldn't process this
  sum1 = 0
  if nums[currentIndex] <= sum:
    sum1 = brute_force(
      nums, sum - nums[currentIndex], currentIndex + 1)

  # recursive call after excluding the number at the currentIndex
  sum2 = brute_force(nums, sum, currentIndex + 1)

  return sum1 + sum2

def top_down_memoization(dp, nums, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1

  n = len(nums)
  if n == 0 or currentIndex >= n:
    return 0

  # check if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    sum1 = 0
    if nums[currentIndex] <= sum:
      sum1 = top_down_memoization(
        dp, nums, sum - nums[currentIndex], currentIndex + 1)

    # recursive call after excluding the number at the currentIndex
    sum2 = top_down_memoization(dp, nums, sum, currentIndex + 1)

    dp[currentIndex][sum] = sum1 + sum2

  return dp[currentIndex][sum]

def bottom_up_dynamic(nums, sum):
  #I am so damn tired
  n = len(nums)
  dp = [[0for x in range(sum+1)] for y in range(n)]

  for i in range(n):
    dp[i][0] = 1 #can get 0 sum from any number via the empty set

  for s in range(1, sum+1):
    dp[0][s] = 1 if nums[0] == s else 0 #if the first number == s, 

  for i in range(1, n):
    for s in range(1, sum+1):
      dp[i][s] = dp[i-1][s] #if we could get this sum without the number x times, we can get it at this index by excluding the same number of times
      if s >= nums[i]: #if number can be safely added
        dp[i][s] += dp[i-1][s-nums[i]] #add the number of times we could get this sum - nums[i] without nums[i]

  return dp[n-1][sum]

def bottom_up_1d_array(nums, sum):
  n = len(nums)
  dp = [0 for x in range(sum+1)]
  dp[0] = 1

  for s in range(1, sum+1):
    dp[s] = 1 if nums[0] == s else 0 #if the first number == s, 

  for i in range(1, n):
    for s in range(sum, -1, -1):
      if s >= nums[i]: #if number can be safely added
        dp[s] += dp[s-nums[i]] #add the number of times we could get this sum - nums[i] without nums[i]

  return dp[sum]

def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
