from heapq import *

def k_most_freq(nums, k):
  num_freq = {}
  for num in nums:
    num_freq[num] = num_freq.get(num, 0) + 1

  min_heap = []

  for num, freq in num_freq.items():
    heappush(min_heap, (freq, num))
    if len(min_heap) > k:
      heappop(min_heap) #remove least frequent number in heap

  result = []
  while min_heap:
    result.append(heappop(min_heap)[1])
  
  return result

def main(): 
  print("Here are the K frequent numbers: " +
        str(k_most_freq([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(k_most_freq([5, 12, 11, 3, 11], 2)))


main()