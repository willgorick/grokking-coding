from heapq import *

class NumberStream:
  def __init__(self, stream=[]):
    self.max_heap = [] #first half of numbers, stored as negatives so the largest number is first
    self.min_heap = [] #second half of numbers

  def insert_num(self, num):
    if not self.max_heap or -self.max_heap[0] >= num:
      heappush(self.max_heap, -num)
    else:
      heappush(self.min_heap, num)
    
    if len(self.max_heap) > len(self.min_heap) + 1: #too many in max heap
      heappush(self.min_heap, -heappop(self.max_heap)) #move largest number from lower half to upper half
    elif len(self.max_heap) < len(self.min_heap):
      heappush(self.max_heap, -heappop(self.min_heap))
    
  def find_median(self):
    if len(self.max_heap) == len(self.min_heap):
      return (-self.max_heap[0] + self.min_heap[0]) / 2.0
    return -self.max_heap[0]
  
def main():
  medianOfAStream = NumberStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()