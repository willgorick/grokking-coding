from heapq import *

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

def next_interval(intervals):
  n = len(intervals)
  max_start_heap, max_end_heap = [], []

  result = [0 for x in range(n)]

  for ind in range(n):
    heappush(max_start_heap, (-intervals[ind].start, ind))
    heappush(max_end_heap, (-intervals[ind].end, ind))

  for _ in range(n):
    top_end, end_ind = heappop(max_end_heap)
    result[end_ind] = -1 #default to -1 if no next interval
    if -max_start_heap[0][0] >= -top_end: #latest avail start time and latest avail end time
      top_start, start_ind = heappop(max_start_heap)
      while max_start_heap and -max_start_heap[0][0] >= -top_end: #keep going to get the interval with a start time closest to the last end
        top_start, start_ind = heappop(max_start_heap)
      result[end_ind] = start_ind
      heappush(max_start_heap, (top_start, start_ind)) #put the interval back so it is available to be chosen again
  return result


def main():
  result = next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()