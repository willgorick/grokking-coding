
def find_all_duplicates(nums):
  i = 0
  while i < len(nums):
    j = nums[i]-1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  duplicate_nums = []
  for i in range(len(nums)):
    if nums[i] != i+1:
      duplicate_nums.append(nums[i])
  return duplicate_nums




def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()