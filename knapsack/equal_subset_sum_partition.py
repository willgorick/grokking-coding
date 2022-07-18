
#can we split the numbers into two groups whose sums are equal.  This problem can be reduced to: can we find any subset of numbers whose sum is equal to half of the total sum
def can_partition(nums):
  s = sum(nums)
  #odd numbers can't be split evenly
  if s%2 != 0:
    return False

  # return brute_force(nums, s/2, 0)

  #initalize the 'dp' array, -1 for default, 1 for true, 0 for false
  #first dimension is different subsets, second dimension is different sums from the subsets
  # dp = [[-1 for x in range(int(s/2) +1)] for y in range(len(nums))]
  # return True if top_down_memoization(dp, nums, int(s/2), 0) == 1 else False

  return bottom_up_dp(nums, s)

def brute_force(nums, sum, ind):
  if sum == 0:
    return True
  
  n = len(nums) # no nums or our index is out of bounds
  if n == 0 or ind >= n:
    return False

  # recursively call the other numbers after choosing our current number, if our current number isn't already greater than the sum
  if nums[ind] <= sum:
    if brute_force(nums, sum - nums[ind], ind + 1):
      return True

  #recursive call after excluding the number at the index
  return brute_force(nums, sum, ind + 1)

def top_down_memoization(dp, nums, sum, ind):
  if sum == 0:
    return 1

  n = len(nums)
  if n == 0 or ind >= n:
    return 0

  # if we haven't solved this problem yet
  if dp[ind][sum] == -1:
    #recursively call all the other numbers after choosing our current number, if our current isn't already greater than the sum
    if nums[ind] <= sum: # if we find a solution with our number return it, otherwise try without
      if top_down_memoization(dp, nums, sum-nums[ind], ind+1) == 1:
        dp[ind][sum] = 1
        return 1
    #recursive call after excluding our current number
    dp[ind][sum] = top_down_memoization(dp, nums, sum, ind+1)

  return dp[ind][sum] #return if there is a sum within this subset equal to half our total sum (for the initial run that is 0)

def bottom_up_dp(nums, s):
  target, n = int(s/2), len(nums)

  dp = [[False for _ in range(target +1)] for _ in range(n)]

  #populate the sum = 0 column, as we can always get '0' sum with an empty set
  for i in range(n):
    dp[i][0] = True
  
  #True only if the first number equals the required sum
  for s in range(1, target + 1):
    dp[0][s] = nums[0] == s

  for i in range(1, n):
    for s in range(1, target + 1):
      #if we can get already get the sum without current number at in 'i'
      if dp[i -1][s]:
        #proceed without the number
        dp[i][s] = dp[i-1][s]
      elif s >= nums[i]: #else if we can find a subset to get the remaining sum
        dp[i][s] = dp[i-1][s - nums[i]] #if we were true for the previous index without this number, at the sum - this number, then we should be true as well

  #answer is in the bottom right corner
  return dp[n-1][s]
  #for each index between 0 and len(nums) and each sum between 0 and big sum /2.  If we exclude the number we can get the sum from dp[i-1][s].  If we include the number we can get the sum from dp[i-1][s-nums[i]]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  # print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  # print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()