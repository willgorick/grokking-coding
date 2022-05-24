def ceiling(nums, key):
  n = len(nums)-1
  if key > nums[n]:
    return -1
  start, end = 0, n
  while start <= end:
    mid = (start + end) // 2
    if key == nums[mid]:
      return mid
    if key > nums[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return start #once start > end, we know we just incremented start so key was greater than prev value, but since start > end it's not greater than start

def floor(nums, key):
  n = len(nums)-1
  if key < nums[0]:
    return -1
  start, end = 0, n
  while start <= end:
    mid = (start + end) // 2
    if key == nums[mid]:
      return mid
    if key > nums[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return end
def main():
  print(ceiling([4, 6, 10], 6))
  print(ceiling([1, 3, 8, 10, 15], 12))
  print(ceiling([4, 6, 10], 17))
  print(ceiling([4, 6, 10], -1))

  print(floor([4, 6, 10], 6))
  print(floor([1, 3, 8, 10, 15], 12))
  print(floor([4, 6, 10], 17))
  print(floor([4, 6, 10], -1))


main()
