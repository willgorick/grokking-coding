def min_subset_sum_diff(nums):
  # return brute_force(nums, 0, 0, 0)

  # s = sum(nums)
  # dp = [[-1 for x in range(s+1)] for y in range(len(nums))]
  # return top_down(dp, nums, 0, 0, 0)

  return bottom_up(nums)

def brute_force(nums, ind, sum1, sum2):
  # base check
  if ind == len(nums):
    return abs(sum1 - sum2)

  # recursive call after including the number at the ind in the first set
  diff1 = brute_force(
    nums, ind + 1, sum1 + nums[ind], sum2)

  # recursive call after including the number at the ind in the second set
  diff2 = brute_force(
    nums, ind + 1, sum1, sum2 + nums[ind])

  return min(diff1, diff2)

def top_down(dp, nums, ind, sum1, sum2):
  if ind == len(nums):
    return abs(sum1 - sum2)

  if dp[ind][sum1] == -1:
    diff1 = top_down(dp, nums, ind+1, sum1 + nums[ind], sum2)

    diff2 = top_down(dp, nums, ind+1, sum1, sum2 + nums[ind])

    dp[ind][sum1] = min(diff1, diff2)

  return dp[ind][sum1]

def bottom_up(nums):
  s = sum(nums)
  n = len(nums)
  target = int(s/2)+1
  dp = [[False for x in range(target)] for y in range(n)]

  # populate the s=0 columns, as we can always form '0' sum with an empty set
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is equal to 
  # that number
  for j in range(0, target):
    dp[0][j] = nums[0] == j

  # process all subsets for all sums
  for i in range(1, n):
    for j in range(1, target):
      # if we can get the sum 's' without the number at index 'i'
      if dp[i - 1][j]:
        dp[i][j] = True
      elif j >= nums[i]:
        # else include the number and see if we can find a subset to get remaining sum
        dp[i][j] = dp[i - 1][j - nums[i]]

  sum1 = 0
  # find the largest index in the last row which is true
  for i in range(target-1, -1, -1):
    if dp[n - 1][i]:
      sum1 = i
      break

  sum2 = s - sum1
  return abs(sum2 - sum1)

def main():
  print("Subset difference: " + str(min_subset_sum_diff([1, 2, 3, 9])))
  print("Subset difference: " + str(min_subset_sum_diff([1, 2, 7, 1, 5])))
  print("Subset difference: " + str(min_subset_sum_diff([1, 3, 100, 4])))


main()