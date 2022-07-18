def subset_sum(nums, target):
  n = len(nums)
  dp = [[False for _ in range(target+1)] for _ in range(n)]

  for i in range(n):
    dp[i][0] = True #any set can get a sum of 0 by excluding numbers

  for s in range(1, target+1):
    dp[0][s] = nums[0] == s #if the first number equals the sum, set it to true

  for i in range(1, n):
    for s in range(1, target+1):
      if dp[i-1][s]: #if the previous index can reach this sum, so can the current index, by excluding the number
        dp[i][s] = True
      elif s >= nums[i]: #nums[i] is not too large to be added to the sum
        dp[i][s] = dp[i-1][s-nums[i]] #if without this number we were equal to the sum - this number, then set this number at this sum to true
  return dp[n-1][target]

#solving the problem with O(s) space
def subset_sum_smaller(nums, target):
  n = len(nums)
  dp = [False for _ in range(target+1)]

  dp[0] = True #we can get sum 0 from empty set

  for s in range(1, target+1):
    dp[s] = nums[0] == s

  for i in range(1, n):
    for s in range(target, -1, -1): #decrement from target to 0
      #if dp[s] == true, we can get the sum without nums[i], so leave it as true.  else see if we can find a subset to equal the remaining sum
      if not dp[s] and s >= nums[i]:
        dp[s] = dp[s-nums[i]] #could get the sum - this number before adding this number?
  return dp[target]

def main():
  print(subset_sum([1,2,3,7], 6))
  print(subset_sum([1,2,7,1], 10))
  print(subset_sum([1,3,4,8], 6))

  print(subset_sum_smaller([1,2,3,7], 6))
  print(subset_sum_smaller([1,2,7,1], 10))
  print(subset_sum_smaller([1,3,4,8], 6))

main()