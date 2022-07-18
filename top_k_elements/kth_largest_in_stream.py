from heapq import *

class Stream:
  def __init__(self, nums, k):
    self.min_heap = [] #k largest numbers in a min heap so the kth largest is at the top
    for i in range(k):
      heappush(self.min_heap, nums[i])
    for i in range(k, len(nums)):
      if nums[i] > self.min_heap[0]:
        heappop(self.min_heap)
        heappush(self.min_heap, nums[i])
    self.k = k
  
  def add(self, num):
    if num > self.min_heap[0]:
      heappop(self.min_heap)
      heappush(self.min_heap, num)
    return self.min_heap[0]

def main():

  kthLargestNumber = Stream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()