from heapq import *
import heapq
import time
def sliding_window_median(nums, k):
  tic = time.perf_counter_ns()
  result = []
  for i in range(len(nums)-k+1):
    curr_window = nums[i:i+k]
    result.append(find_median(curr_window))
  toc = time.perf_counter_ns()
  print(toc-tic)
  return result 

def find_median(nums):
  length = len(nums)
  nums.sort()
  if length %2 == 1: #odd number: return the middle number
    return nums[length//2]
  else: 
    return (nums[length//2] + nums[length//2-1])/2

class SlidingWindowMedian:
  def __init__(self):
    self.max_heap, self.min_heap = [], []
  
  def find_sliding_window_median(self, nums, k):
    tic = time.perf_counter_ns()
    result = [0.0 for x in range(len(nums)-k+1)]
    for i in range(0, len(nums)):
      if not self.max_heap or nums[i] <= -self.max_heap[0]:
        heappush(self.max_heap, -nums[i])
      else:
        heappush(self.min_heap, nums[i])
      self.rebalance_heaps()

      if i-k +1 >= 0: # we have at least k elements in the window
        if len(self.max_heap) == len(self.min_heap): #even number
          result[i-k+1] = (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
          result[i-k+1] = -self.max_heap[0]
        remove_elem = nums[i-k+1] #after setting the median value, remove the element at the left edge of window
        if remove_elem <= -self.max_heap[0]: #check if in max heap
          self.remove(self.max_heap, -remove_elem)
        else: 
          self.remove(self.min_heap, remove_elem) #in min heap
        
        self.rebalance_heaps()
    toc = time.perf_counter_ns()
    print(toc-tic)
    return result

  def remove(self, heap, element):
    ind = heap.index(element)
    heap[ind] = heap[-1]
    del heap[-1]
    if ind < len(heap):
      heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)


  def rebalance_heaps(self):
    if len(self.max_heap) > len(self.min_heap) +1:
      heappush(self.min_heap, -heappop(self.max_heap))
    elif len(self.max_heap) < len(self.min_heap):
      heappush(self.max_heap, -heappop(self.min_heap))



def main():

  print(sliding_window_median([1, 2, -1, 3, 5], 2))
  print(sliding_window_median([1, 2, -1, 3, 5], 3))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))

main()