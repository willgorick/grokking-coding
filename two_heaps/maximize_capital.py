from heapq import *

def find_max_cap(capital, profits, num_projects, initial_cap):
  min_cap_heap = []
  max_prof_heap = []

  for i in range(len(profits)):
    heappush(min_cap_heap, (capital[i], i)) #heap will automatically sort by the first element of the tuple
  available_cap = initial_cap
  for _ in range(num_projects):
    while min_cap_heap and min_cap_heap[0][0] <= available_cap: #til the end of the heap, if the next highest heap has a cap value less than or equal to our available, add it to our profit heap
      capital, i = heappop(min_cap_heap)
      heappush(max_prof_heap, (-profits[i], i)) #has to be negative for max heap
      
    if not max_prof_heap: #no projects left that we have enough capital for
      break
      
    available_cap += -heappop(max_prof_heap)[0]
  return available_cap


def main():

  print("Maximum capital: " +
        str(find_max_cap([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_max_cap([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
