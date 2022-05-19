import math

def shortest_window_sort(arr):
  low, high = 0, len(arr)-1

  while (low < len(arr)-1 and arr[low] <= arr[low + 1]):
    low += 1
  if low == len(arr) -1:
    return 0

  while (high > 0 and arr[high] >= arr[high-1]):
    high -= 1

  #now we have our initial bounds
  sub_max = -math.inf
  sub_min = math.inf

  for i in range(low, high+1):
    sub_max = max(sub_max, arr[i])
    sub_min = min(sub_min, arr[i])
  
  while (low > 0 and arr[low-1] > sub_min): # this works because below the initial low pointer, and above the initial high pointer, the values are sorted
    low -= 1
  while (high < len(arr)-1 and arr[high+1] < sub_max): # 
    high += 1

  return high-low+1

def main():
  print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(shortest_window_sort([1, 2, 3]))
  print(shortest_window_sort([3, 2, 1]))
  print(shortest_window_sort([1, 2, 9, 12, 5, 3, 7, 15, 2, 9, 12]))

main()