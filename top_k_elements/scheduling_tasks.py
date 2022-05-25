from heapq import *

def schedule_tasks(tasks, k):
  result = 0
  task_freq = {}
  for task in tasks:
    task_freq[task] = task_freq.get(task, 0) + 1

  max_heap = []
  for task, freq in task_freq.items():
    heappush(max_heap, (-freq, task))
  
  while max_heap:
    wait_list = []
    n = k + 1
    while n > 0 and max_heap: #this is k intervals
      result += 1
      freq, char = heappop(max_heap)
      if -freq > 1:  #still more of this task left
        wait_list.append((freq+1, char))
      n -= 1

    for freq, char in wait_list: #now that k intervals have passed, add those tasks back to the heap
      heappush(max_heap, (freq, char))
    
    if max_heap: #if our heap ran out before n got to zero, we need to add that many intervals of idling to our result
      result += n

  return result

def main():
  print(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2))
  print(schedule_tasks(['a', 'b', 'a'], 3))
main()