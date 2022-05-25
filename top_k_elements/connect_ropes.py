from heapq import *

def connect_ropes(ropes):
  if len(ropes) < 2:
    return ropes[0]
  heap = []
  for rope in ropes:
    heappush(heap, rope)

  min_cost = 0
  while len(heap) > 1:
    connect = heappop(heap) + heappop(heap)
    min_cost += connect
    heappush(heap, connect)
  return min_cost

def main():
  print(connect_ropes([1, 3, 11, 5]))
  print(connect_ropes([3, 4, 5, 6]))
  print(connect_ropes([1, 3, 11, 5, 2]))
main()