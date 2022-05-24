
def binary_search(nums, key):
  start, end = 0, len(nums)-1
  is_ascending = nums[start] < nums[end] #figure out which way it's sorted
  while start <= end:
    mid = (start + end) // 2
    mid_val = nums[mid]
    if key == nums[mid]:
      return mid
    if is_ascending:
      if key < mid_val:
        end = mid -1
      else:
        start = mid + 1
    else:
      if key > mid_val:
        end = mid - 1
      else:
        start = mid + 1
  return -1

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()