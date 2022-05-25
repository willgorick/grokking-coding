from heapq import *

def median(lists):
  total_len = 0
  heap = []
  for list in lists:
    total_len += len(list)
  even = total_len % 2 == 0 
  median = (total_len // 2)+1 if even else total_len // 2 #median for even numbers is the second median number, we'll keep track of the first with prev_number
  for i in range(len(lists)):
    heappush(heap, (lists[i][0], 0, lists[i]))

  number = 0
  while heap:
    number, i, list = heappop(heap)
    median -= 1
    if median == 0:
      if even:
        return (prev_number + number) / 2
      else:
        return number
    if len(list) > i+1:
      heappush(heap, (list[i+1], i+1, list))
    prev_number = number
  return False

def main():
  print("Median is: " + str(median([[2, 6, 8], [3, 6, 7], [1, 3, 4]]))) 
  #1 2 3 3 4 6 6 7 8

  print("Median is: " + str(median([[2, 6, 8], [3, 6, 7], [1, 3]]))) 
  #1 2 3 3 6 6 7 8


main()