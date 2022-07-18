from heapq import *

def top_k_numbers(nums, k):
  result = []
  for i in range(k):
    heappush(result, nums[i])
  for i in range(k, len(nums)):
    if result[0] < nums[i]: #if current number is larger than smallest in our heap
      heappop(result)
      heappush(result, nums[i])
  return result

def main():
  print(top_k_numbers([3, 1, 5, 12, 2, 11], 3))
  print(top_k_numbers([5, 12, 11, -1, 12], 3))

main()