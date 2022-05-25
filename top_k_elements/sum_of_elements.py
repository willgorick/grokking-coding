from heapq import *

def sum_elements(nums, k1, k2):
  min_heap = []
  result = 0
  
  for num in nums:
    heappush(min_heap, num)

  for _ in range(k1):
    heappop(min_heap)

  for _ in range(k1+1, k2):
    result += heappop(min_heap)

  return result

def sum_elements_max_heap(nums, k1, k2):
  max_heap = []
  for i in range(len(nums)):
    if i < k2 - 1:
      heappush(max_heap, -nums[i])
    elif nums[i] < - max_heap[0]:
      heappop(max_heap)
      heappush(max_heap, -nums[i])

  result = 0
  for _ in range(k2 - k1 -1): #the numbers between k2 and k1
    result += -heappop(max_heap)
  
  return result

def main():
  print(sum_elements([1, 3, 12, 5, 15, 11], 3, 6))
  print(sum_elements([3, 5, 8, 7], 1, 4))

  print(sum_elements_max_heap([1, 3, 12, 5, 15, 11], 3, 6))
  print(sum_elements_max_heap([3, 5, 8, 7], 1, 4))

main()