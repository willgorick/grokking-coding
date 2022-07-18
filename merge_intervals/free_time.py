
from heapq import *


class Interval:
  def __init__(self, start, end):
      self.start = start
      self.end = end
  
  def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class EmployeeInterval:
  def __init__(self, interval, employee_index, interval_index):
    self.interval = interval
    self.employee_index = employee_index
    self.interval_index = interval_index

  def __lt__(self, other):
    return self.interval.start < other.interval.start

def find_free_time(schedule):
  if schedule is None or len(schedule) < 1:
    return []

  n = len(schedule)
  result, min_heap = [], []

  for i in range(n):
    heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0)) #heappush everyone's first interval

  prev_int = min_heap[0].interval
  while min_heap:
    top = heappop(min_heap)
    if prev_int.end < top.interval.start: #no overlap between previous and current
      result.append(Interval(prev_int.end, top.interval.start)) #time between prev interval end and current interval start
      prev_int = top.interval
    else: #intervals overlap, update prev interval to earlier if current ends earlier
      if prev_int.end < top.interval.end: #basically make sure ending of our interval is the later of the two
        prev_int = top.interval
    employee_sched = schedule[top.employee_index]
    if len(employee_sched) > top.interval_index + 1: #if this employee has more intervals, push their next one to the queue
      heappush(min_heap, EmployeeInterval(employee_sched[top.interval_index +1], top.employee_index, top.interval_index+1))
  return result
  
def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_free_time(input):
        interval.print_interval()
    print()


main()