from heapq import *;

class Job:
  def __init__(self, start, end, load):
    self.start = start
    self.end = end
    self.load = load
  def __lt__(self, other):
    self.end < other.end

def max_load(jobs):
  jobs.sort(key=lambda x: x.start)
  max_load, curr_load = 0, 0
  min_heap = []
  for j in jobs:
    while len(min_heap) > 0 and j.start >= min_heap[0].end: #remove all jobs that ended before current job starts, but first decrement their load from our curr_load
      curr_load -= min_heap[0].load
      heappop(min_heap)
    heappush(min_heap, j)
    curr_load += j.load
    max_load = max(max_load, curr_load)
  return max_load

def main():
  print("Maximum CPU load at any time: " + 
             str(max_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + 
             str(max_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + 
             str(max_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))
main()