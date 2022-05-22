def corrupt_pair(nums):
  i = 0
  while i < len(nums):
    j = nums[i]-1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else: 
      i += 1
  for i in range(len(nums)):
    if nums[i] != i+1:
      return [nums[i], i+1]
  return [-1, -1] #no corrupt pairs found


def main():
  print(corrupt_pair([3, 1, 2, 5, 2]))
  print(corrupt_pair([3, 1, 2, 3, 6, 4]))
  print(corrupt_pair([6, 5, 1, 2, 2, 4]))


main()
