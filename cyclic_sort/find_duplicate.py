def find_duplicate(nums):
  i = 0
  while i < len(nums):
    j = nums[i]-1
    if nums[i] != nums[j]:
      nums[j], nums[i] = nums[i], nums[j]
    else:
      if i == nums[i]: #the numbers were swapped previously, meaning they should be sorted but the number is one spot past where it should be 
        return nums[i]
      i += 1
  return nums

def find_duplicate_without_modifying(nums):
  slow, fast = nums[0], nums[nums[0]]
  while slow != fast:
    slow = nums[slow]
    fast = nums[nums[fast]]
  current = nums[nums[slow]]
  cycle_len = 1
  while current != nums[slow]:
    current = nums[current]
    cycle_len += 1
  
  return find_start(nums, cycle_len)

def find_start(nums, cycle_len):
  pointer1, pointer2 = nums[0], nums[0]
  while cycle_len > 0:
    pointer2 = nums[pointer2]
    cycle_len -= 1
  
  while pointer1 != pointer2:
    pointer1 = nums[pointer1]
    pointer2 = nums[pointer2]

  return pointer1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))

  print(find_duplicate_without_modifying([1, 4, 4, 3, 2]))
  print(find_duplicate_without_modifying([2, 1, 3, 3, 5, 4]))
  print(find_duplicate_without_modifying([2, 4, 1, 4, 4]))

main()