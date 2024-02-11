"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Time Complexity: O(N+M) where N is the lenght of one interval list and M is the length of the other
Space Complexity: O(N+M) for the result list, otherwise O(1)

"""
class Interval:
  def __init__(self, start, end):
   self.start = start
   self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
  def intervals_intersection(self, intervals_a, intervals_b):
    result = []
    #starting indices for each interval list
    i, j = 0, 0

    while i < len(intervals_a) and j < len(intervals_b):
        int_a = intervals_a[i]
        int_b = intervals_b[j]

        # a start lies within b interval
        a_overlaps_b = int_a.start >= int_b.start and int_a.start <= int_b.end
        #b start lies within a interval
        b_overlaps_a = int_b.start >= int_a.start and int_b.start <= int_a.end

        #if either overlap, append based on max of the starts and min of the ends
        if (a_overlaps_b or b_overlaps_a):
            result.append(Interval(max(int_a.start, int_b.start), min(int_a.end, int_b.end)))
        
        #go to the next interval based on which interval ends earlier
        if int_a.end < int_b.end:
            i += 1
        else:
            j += 1

    return result




def main():
  sol = Solution()
  intervals_a = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
  intervals_b = [Interval(2, 3), Interval(5, 7)]
  print("Intervals Intersection: ", end="")
  for i in sol.intervals_intersection(intervals_a,intervals_b):
      i.print_interval()
      print(" ", end="")
  print()


  intervals_a = [Interval(1, 3), Interval(5, 7), Interval(9, 12)]
  intervals_b = [Interval(5, 10)]
  print("Intervals Intersection: ", end="")
  for i in sol.intervals_intersection(intervals_a,intervals_b):
      i.print_interval()
      print(" ", end="")
  print()
  

main()