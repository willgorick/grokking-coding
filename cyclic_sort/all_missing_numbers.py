
def all_missing_nums(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1 #index where nums[i] shoud be
    if nums[i] != nums[j]:  #if they're equal, that means either it's already sorted, or we found a duplicate, and we can move on....can't just use i != j here because of the duplicates
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  missing = []
  for i in range(len(nums)):
    if nums[i]-1 != i: #if we had a 4, there wouldn't be an 8 there
      missing.append(i+1)
  return missing



def main():
  print(all_missing_nums([2, 3, 1, 8, 2, 3, 5, 1]))
  print(all_missing_nums([2, 4, 1, 2]))
  print(all_missing_nums([2, 3, 2, 1]))


main()