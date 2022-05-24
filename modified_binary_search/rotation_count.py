
def rotation_count(arr):
  start, end = 0 , len(arr)-1
  while start < end:
    mid = (start + end) // 2
    if arr[mid] > arr[mid+1]:
      return mid+1
    if arr[mid-1] > arr[mid]:
      return mid

    if arr[start] == arr[mid] == arr[end]: #handle duplicates
      if arr[start] > arr[start+1]:
        return start +1
      start += 1
      if arr[end-1] > arr[end]:
        return end
      end -= 1
    elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]): #left is sorted, pivot is on the right
      start = mid + 1
    else: #right is sorted, pivot is on the left
      end = mid - 1
  return 0

def main():
  print(rotation_count([10, 15, 1, 3, 8]))
  print(rotation_count([4, 5, 7, 9, 10, -1, 2]))
  print(rotation_count([1, 3, 8, 10, 15]))

main()