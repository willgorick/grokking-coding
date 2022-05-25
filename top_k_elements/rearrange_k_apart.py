from heapq import *
from collections import deque

def rearrange(string, k):
  if k <= 1:
    return string

  char_freq, max_heap = {}, []
  for x in string:
    char_freq[x] = char_freq.get(x, 0) + 1
  
  for char, freq in char_freq.items():
    heappush(max_heap, (-freq, char))
  
  i = 0
  result = []
  queue = deque()
  while max_heap:
    i += 1
    freq, char = heappop(max_heap)
    # if we've gone through k, add back element from queue
    if i >= k:
      prev_freq, prev_char = queue.popleft()
      if -prev_freq > 0: #only push to heap if it still has more frequency
        heappush(max_heap, (prev_freq, prev_char))
    # append current character to string and decrement its count
    result.append(char)
    queue.append((freq+1, char))
  
  return ''.join(result) if len(result) == len(string) else False


def main():
  print(rearrange("mmpp", 2))
  print(rearrange("Programming", 3))
  print(rearrange("aab", 2))
  print(rearrange("aapa", 3))

main()