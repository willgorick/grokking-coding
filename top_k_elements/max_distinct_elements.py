from heapq import *

def max_distinct(nums, k):
  if len(nums) <= k:
    return 0

  distinct_elems = 0
  num_freq = {}
  min_heap = []
  for num in nums:
    num_freq[num] = num_freq.get(num, 0) + 1
  for num, count in num_freq.items():
    if count > 1: #we only need to worry about numbers that are not already distinct
      if len(min_heap) < k:
        heappush(min_heap, (count, num))
    else:
      distinct_elems += 1
  while k > 0 and min_heap:
    count, num = heappop(min_heap)
    k -= count -1 #need to keep one to be distinct
    if k >= 0: # we still have k's to go so subtract one...if we are out of k's that means that we weren't able to remove enough to get this number to be distinct
      distinct_elems += 1
  if k > 0: #haven't removed enough
    distinct_elems -= k #just have to remove distinct elems to get to k
  
  return distinct_elems

def main():
  print(max_distinct([7, 3, 5, 8, 5, 3, 3], 2))
  print(max_distinct([3, 5, 12, 11, 12], 3))
  print(max_distinct([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))

main()