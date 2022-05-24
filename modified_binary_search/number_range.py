def find_range(arr, key):
  result = [-1, -1]
  result[0] = binary_search(arr, key, False)
  if result[0] != -1: #only search if key found in array
    result[1] = binary_search(arr, key, True)
  return result

def binary_search(arr, key, find_max):
  key_ind = -1
  start, end = 0, len(arr)-1
  while start <= end:
    mid = (start + end) // 2
    if key == arr[mid]:
      key_ind = mid
      if find_max: #continue searching to find last ind of key
        start = mid+1
      else: #search for first index of key
        end = mid - 1
    elif key < arr[mid]:
      end = mid - 1 
    else:
      start = mid + 1
  return key_ind

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))

main()