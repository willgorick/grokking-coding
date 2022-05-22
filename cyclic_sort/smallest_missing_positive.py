def smallest_missing_positive(nums): 
  i = 0
  while i < len(nums):
    j = nums[i]-1
    if nums[i] > 0 and nums[i] <= len(nums) and nums[j] != nums[i]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  for i in range(len(nums)):
    if nums[i] != i+1:
      return i+1
  return len(nums) + 1

def main():
  print(smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(smallest_missing_positive([3, -2, 0, 1, 2]))
  print(smallest_missing_positive([3, 2, 5, 1]))
  print(smallest_missing_positive([33, 37, 5]))

main()