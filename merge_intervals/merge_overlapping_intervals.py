class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end
  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end="")

def merge_overlapping_intervals(intervals):
  if len(intervals) < 2: #need multiple intervals to merge
    return intervals

  intervals.sort(key=lambda x: x.start) #sort by start interval

  merged_intervals = []
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1, len(intervals)): #basically second interval through the end
    interval = intervals[i]
    if interval.start <= end: #overlapping prevous, merge this interval with the previous
      end = max(end, interval.end)
    else: #not-overlapping previous, add previous interval to array, then set our start/end to the current interval
      merged_intervals.append(Interval(start, end))
      start = interval.start
      end = interval.end
  merged_intervals.append(Interval(start, end))
  return merged_intervals

def main():
  print("Merged intervals: ", end='')
  intervals = merge_overlapping_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)])
  for ind, interval in enumerate(intervals): 
    interval.print_interval()
    if ind < len(intervals)-1:
      print(", ", end="")
  print()

  print("Merged intervals: ", end='')
  intervals = merge_overlapping_intervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)])
  for ind, interval in enumerate(intervals): 
    interval.print_interval()
    if ind < len(intervals)-1:
      print(", ", end="")
  print()

  print("Merged intervals: ", end='')
  intervals = merge_overlapping_intervals([Interval(1, 4), Interval(2, 6), Interval(3, 5)])
  for ind, interval in enumerate(intervals): 
    interval.print_interval()
    if ind < len(intervals)-1:
      print(", ", end="")
  print()
main()