from heapq import *

def top_k_numbers(nums, k):
  result = []
  for i in range(k):
    heappush(result, nums[i])
  for i in range(k, len(nums)):
    if result[0] < nums[i]:
      heappop(result)
      heappush(result, nums[i])
    #if the smallest number in our heap is bigger than the current number, leave it in the heap
  return result

def main():
  print(top_k_numbers([3, 1, 5, 12, 2, 11], 3))
  print(top_k_numbers([5, 12, 11, -1, 12], 3))

main()