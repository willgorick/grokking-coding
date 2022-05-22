def cyclic_sort(arr):
  for i in range(len(arr)):
    while arr[i]-1 != i:
      swap = arr[arr[i]-1]
      arr[arr[i]-1] = arr[i]
      arr[i] = swap
  return arr

def cyclic_sort2(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      print(nums[i], i)
      i += 1
  return nums

def main():
  print(cyclic_sort2([3, 1, 5, 4, 2]))
  # print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  # print(cyclic_sort([1, 5, 6, 4, 3, 2]))
  # print(cyclic_sort([1, 5, 6, 4, 3, 2]))

main()