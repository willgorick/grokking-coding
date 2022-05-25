from heapq import *

def k_smallest_in_m(lists, k):
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
  print(k_smallest_in_m([[2,6,8], [3,6,7], [1,3,4]], 5))
  print(k_smallest_in_m([[5,8,9], [1,7]], 3))

main()