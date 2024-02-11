"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Time Complexity: O(n log n) - the initial sort is the asymptotically slowest operation, the main loop is linear
Space Complexity: O(n) if all intervals do not overlap the result will be a list of size N (sorting also typically takes O(n))

"""

class Interval:
  def __init__(self, start, end):
   self.start = start
   self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
  def merge_intervals(self, intervals):
    if len(intervals) == 0:
      return []
    result = []
    #sort by interval starts
    intervals.sort(key=lambda x: x.start)
    previous_interval = intervals[0]

    #because of sorting, we guarantee that each previous interval has a start time <= the current one
    for i in range(1, len(intervals)):
      curr_interval = intervals[i]
      #intervals overlap, adjust end to be the max of the two
      if curr_interval.start <= previous_interval.end:
        previous_interval.end = max(previous_interval.end, curr_interval.end)
      #intervals do not overlap
      else:
        result.append(previous_interval)
        previous_interval = curr_interval
      
    #add the last interval to our list
    result.append(previous_interval)
      
    return result


def main():
  sol = Solution()
  print("Merged intervals: ", end='')
  for i in sol.merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in sol.merge_intervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in sol.merge_intervals([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

  

  

main()