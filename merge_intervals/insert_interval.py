
def insert_interval(intervals, new_interval):
  start = new_interval[0]
  end = new_interval[1]
  merged = []
  prev_merge = False
  for i in range(len(intervals)):
    if intervals[i][1] < start:
      merged.append(intervals[i])
      prev_merge = False
      continue
    if intervals[i][0] > end:
      merged.append([start, end])
      merged.append(intervals[i])
      prev_merge = False
      continue

    intervals[i][0] = min(intervals[i][0], start)
    intervals[i][1] = max(intervals[i][1], end)

    start = intervals[i][0]
    end = intervals[i][1]
    prev_merge = True
  if prev_merge:
    merged.append([start, end])

  return merged

def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1

  # skip (and add to output) all intervals that come before the 'new_interval'
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
    merged.append(intervals[i])
    i += 1

  # merge all intervals that overlap with 'new_interval'
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
    new_interval[start] = min(intervals[i][start], new_interval[start])
    new_interval[end] = max(intervals[i][end], new_interval[end])
    i += 1

  # insert the new_interval
  merged.append(new_interval)

  # add all the remaining intervals to the output
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1

  return merged

def main():
  print("Intervals after inserting the new interval: " + 
           str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + 
           str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + 
           str(insert_interval([[2, 3], [5, 7]], [1, 4])))

  print("Intervals after inserting the new interval: " + 
           str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + 
           str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + 
           str(insert([[2, 3], [5, 7]], [1, 4])))

main()