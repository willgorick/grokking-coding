
def min_difference(arr, key):
  if key < arr[0]:
    return arr[0]
  n = len(arr)
  if key > arr[n-1]:
    return arr[n-1]
  start, end = 0, n-1
  while start <= end:
    mid = (start + end) // 2
    if key == arr[mid]:
      return key
    if key > arr[mid]:
      start = mid + 1
    else:
      end = mid - 1

  #at the end of loop, start = end+1
  if (arr[start] - key) < (key - arr[end]):
    return arr[start]
  return arr[end]

def main():
  print(min_difference([4, 6, 10], 7))
  print(min_difference([4, 6, 10], 4))
  print(min_difference([4, 6, 10], 17))
  print(min_difference([1, 3, 4, 10, 15], 12))

main()