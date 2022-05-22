def find_first_k_missing_positive(nums, k):
  i, n = 0, len(nums)
  missing = []
  while i < n:
    j = nums[i]-1
    if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  extra_nums = set()
  for x in range(len(nums)):
    if nums[x] != x + 1:
      missing.append(x+1)
      extra_nums.add(nums[x])
      if len(missing) == k:
        return missing
  i  = 1
  while len(missing) < k:
    candidate = n+i
    if candidate not in extra_nums:
      missing.append(candidate)
    i += 1
  return missing

def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))
  print(find_first_k_missing_positive([2, 1, 3, 6, 5], 2))

main()