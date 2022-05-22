def missing_number(nums):
  i, n  = 0, len(nums)
  while i < n:
    j = nums[i] # j = 3
    if j < n and j != nums[j]: #only sorting 0 - (n-1)
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
    print(nums, i)
  for i in range(n):
    if nums[i] != i: #we were unable to put the correct number here, meaning that number is missing
      return i

  return n # if we didn't find it, then it's the last digit that's missing


def main():
  print(missing_number([4, 0, 3, 1]))
  print(missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()