from heapq import *

def find_Kth_smallest(lists, k):
  min_heap = []

  for i in range(len(lists)):
    heappush(min_heap, (lists[i][0], 0, lists[i])) #number, index in list, which list

  while min_heap:
    num, i , list = heappop(min_heap)
    k -= 1
    if k == 0:
      return num
    if len(list) > i+1:
      heappush(min_heap, (list[i+1], i+1, list))

  return False #not k numbers in the lists

def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()