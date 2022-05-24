from encodings import search_function


def search_bitonic_array(arr, key):
  max_ind = find_max(arr)
  key_ind = binary_search(arr, key, 0, max_ind)
  if key_ind != -1:
    return key_ind #found in the first half
  return binary_search(arr, key, max_ind +1, len(arr)-1)

def find_max(arr):
  start, end = 0, len(arr)-1
  while start < end: #stop when equal
    mid = (start + end) // 2
    if arr[mid] > arr[mid+1]:
      end = mid
    else:
      start = mid +1
  return start #start = end

def binary_search(arr, key, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
      return mid
    if arr[start] < arr[end]: #ascending
      if key < arr[mid]:
        end = mid -1
      else:
        start = mid + 1
    else: #descending
      if key > arr[mid]:
        end = mid - 1
      else:
        start = mid + 1
  return -1 

def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))
  print(search_bitonic_array([10, 9, 8], 7))

main()