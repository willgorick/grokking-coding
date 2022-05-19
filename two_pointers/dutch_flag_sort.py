
def dutch_flag_sort(arr): #two pointers, the idea is to move all 0's before 1 and all 2's after high
  low = 0
  high = len(arr)-1
  i = 0
  while i <= high:
    if arr[i] == 0: #swap the value at i with the value at the low pointer so it's below
      arr[i], arr[low] = arr[low], arr[i]
      i += 1
      low += 1 #to account for the new 0 at that location
    elif arr[i] == 1:
      i += 1
    else: #arr[i] == 2
      arr[i], arr[high] = arr[high], arr[i]
      high -= 1

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)


main()