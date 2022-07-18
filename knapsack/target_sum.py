# Sum(some set1) - Sum(some set 2) = S
# We also know that Sum(s1) + Sum(s2) = Sum(nums)
# Therefore Sum(s1) + Sum(s2) + Sum(s1) - Sum(s2) = Sum(nums) + S
# 2Sum(s1) = Sum(nums) + S
# Sum(s1) = (Sum(nums) + S) / 2
# So we must find the count of subsets whose sums is equal to (Sum(nums) + S) / 2

def find_target_subsets(nums, s):

  total_sum = sum(nums) 
  #if (s + sum(nums)) is odd, we can't find a subset equal to half of it
  if total_sum < s or (s + total_sum) %2 == 1:
    return 0

  # return count_subsets_dp(nums, (s + total_sum) // 2)
  return count_subsets_dp_1d(nums, (s + total_sum) // 2)


def count_subsets_dp(nums, s):
  n = len(nums)
  dp = [[0 for _ in range(s+1)] for _ in range(n)]

  #0 sum column always has 1, the empty set
  for i in range(n):
    dp[i][0] = 1

  for s in range(1, s+1):
    dp[0][s] = 1 if nums[0] == s else 0

  for i in range(1, n):
    for s in range(1, s+1):
      dp[i][s] = dp[i-1][s]
      if s >= nums[i]:
        dp[i][s] += dp[i-1][s-nums[i]]

  return dp[n-1][s]

def count_subsets_dp_1d(nums, target):
  n = len(nums)
  dp = [0 for i in range(target+1)]

  #0 sum column always has 1, the empty set
  dp[0] = 1

  for s in range(1, target+1):
    dp[s] = 1 if nums[0] == s else 0

  for i in range(1, n):
    for s in range(target, -1, -1):
      if s >= nums[i]:
        dp[s] += dp[s-nums[i]]

  return dp[target]

def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()  