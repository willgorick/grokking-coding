
def search_rotated_array(arr, key):
  start, end = 0, len(arr)-1
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
      return mid
    #this is the special case to handle duplicate numbers:
    if arr[start] == arr[mid] == arr[end]:
      start += 1
      end -= 1
    if arr[start] <= arr[mid]: #left side is ascending
      if key >= arr[start] and key < arr[mid]: #key in this range
        end = mid -1
      else:
        start = mid + 1
    else: #right side is ascending
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      else:
        end = mid -1
  return -1

def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
  print(search_rotated_array([3, 7, 3, 3, 3], 7))

main()
