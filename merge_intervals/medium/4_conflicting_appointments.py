"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Time Complexity: O(n log n) for the sorting, the actual algorithm is O(n) in order to compare each interval to the previous one
Space Complexity: O(n) for sorting, otherwise O(1)

"""
class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print(f"[{str(self.start)}, {str(self.end)}]", end='')

class Solution:
  def conflicting_appointments(self, intervals):
    intervals.sort(key=lambda x: x.start)
    for i in range(1, len(intervals)):
      #overlap
      if intervals[i-1].end > intervals[i].start:
        return False
        
    return True
  
  def find_all_conflicting_appointments(self, intervals):
    conflicts = []
    intervals.sort(key=lambda x: x.start)
    previous = intervals[0]
    for i in range(1, len(intervals)):
      #overlap
      if previous.end > intervals[i].start:
        conflicts.append([previous, intervals[i]])
        prevoius = Interval(min(previous.start, intervals[i].start), max(previous.end, intervals[i].end))
      else:
        previous = intervals[i]
    for conflict in conflicts:
      print(f"[{conflict[0].start}, {conflict[0].end}] and [{conflict[1].start}, {conflict[1].end}] conflict")
    return conflicts


def main():
  sol = Solution()
  print("Can attend all appointments: " + 
    str(sol.conflicting_appointments([Interval(1, 4), Interval(2, 5), Interval(7, 9)])))
  print("Can attend all appointments: " + 
    str(sol.conflicting_appointments([Interval(6, 7), Interval(2, 4),Interval(8, 12)])))
  print("Can attend all appointments: " + 
    str(sol.conflicting_appointments([Interval(4, 5), Interval(2, 3), Interval(3, 6)])))

  sol.find_all_conflicting_appointments([Interval(4, 5), Interval(2, 3), Interval(3, 6), Interval(5, 7), Interval(7, 8)])

main()
