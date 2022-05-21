def merge(intervals_a, intervals_b):
  result = []
  i, j, start, end = 0, 0, 0, 1
  while i < len(intervals_a) and j < len(intervals_b):
    a_start = intervals_a[i][start]
    a_end = intervals_a[i][end]
    b_start = intervals_b[j][start]
    b_end = intervals_b[j][end]

    a_overlaps_b = a_start >= b_start and a_start <= b_end #a starts after b start and before b ends

    b_overlaps_a = b_start >= a_start and b_start <= a_end #b starts after a start and before a ends

    if (a_overlaps_b or b_overlaps_a):
      result.append([max(a_start, b_start), min(a_end, b_end)])
    if a_end < b_end: #move to next interval of whichever interval set ends earlier
      i += 1
    else:
      j += 1
  return result

def main():
  print("Intervals Intersection: " + 
             str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + 
             str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()