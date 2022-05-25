from heapq import *
from collections import deque

def k_closest(nums, k, x):
  index = binary_search(nums, x)

  return k_closest_pointer(index, nums, k, x)
  return k_closest_heap(index, nums, k, x)
  

def k_closest_heap(index, nums, k, x):
  low, high = index - k, index + k
    
  #make sure high and low are in bounds
  low = max(low, 0) 
  high = min(high, len(nums)-1)

  min_heap = []

  for i in range(low, high+1):
    heappush(min_heap, (abs(nums[i] - x), nums[i])) #store in heap by difference from x

  result = []
  for _ in range(k):
    result.append(heappop(min_heap)[1])
  result.sort()

  return result

def k_closest_pointer(index, nums, k, x):
  p1, p2 = index, index + 1
  result = deque()
  for _ in range(k):
    if p1 >= 0 and p2 < len(nums):
      if abs(nums[p1] - x) <= abs(nums[p2] - x):
        result.appendleft(nums[p1])
        p1 -= 1
      else:
        result.append(nums[p2])
        p2 += 1
    elif p1 >= 0:
      result.appendleft(nums[p1])
      p1 -= 1
    elif p2 < len(nums):
      result.append(nums[p2])
      p2 += 1
  return list(result)
      
def binary_search(nums, x):
  start, index, end = 0, 0, len(nums)-1
  while start <= end:
    mid = (start + end) // 2
    if x == nums[mid]:
      index = mid
      break
    if x > nums[mid]:
      start = mid + 1
    else:
      end = mid - 1
    if abs(nums[mid] - x) < abs(nums[index] - x): #if mid is closer than best so far, set index to mid
      index = mid
  return index
def main():
  print(k_closest([5, 6, 7, 8, 9], 3, 7))
  print(k_closest([2, 4, 5, 6, 9], 3, 6))
  print(k_closest([2, 4, 5, 6, 9], 3, 7))

main()