#smallest range that includes at least one number from each of the M lists
from heapq import *
import math

def find_smallest_range(lists):
  min_heap = []
  start, end = 0, math.inf
  curr_max = -math.inf #this max is only ever set to numbers in the heap

  #put first element from each array into heap
  for arr in lists:
    heappush(min_heap, (arr[0], 0, arr)) #number, index, list
    curr_max = max(curr_max, arr[0]) #max is largest of three starting numbers

  #take smallest element from min heap, if it gives us a smaller range, update the range, add  next element from array if present
  while len(min_heap) == len(lists):
    num, i, arr = heappop(min_heap)
    if end - start > curr_max - num: #we found a smaller min range, betwen our largest number so far and the newest min from the heap
      start = num
      end = curr_max

    if len(arr) > i+1:
      heappush(min_heap, (arr[i+1], i+1, arr))
      curr_max = max(curr_max, arr[i+1])

  return [start, end]

def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()