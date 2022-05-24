def bitonic_array_max(arr):
  start, end = 0, len(arr)-1

  while start < end:
    mid = (start + end) // 2
    if arr[mid] > arr[mid+1]:
      end = mid #decreaasing, so set end to higher num
    else: #increasing, so set start to higher num
      start = mid+1
  return arr[start] #when start = end

def main():
  print(bitonic_array_max([1, 3, 8, 12, 4, 2]))
  print(bitonic_array_max([3, 8, 3, 1]))
  print(bitonic_array_max([1, 3, 8, 12]))
  print(bitonic_array_max([10, 9, 8]))

main()