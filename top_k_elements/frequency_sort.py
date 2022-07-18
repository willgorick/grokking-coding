from heapq import *

def freq_sort(letters):
  freq_map = {}
  max_heap, result = [], []
  for x in letters:
    freq_map[x] = freq_map.get(x, 0) + 1
  
  for letter, count in freq_map.items():
    heappush(max_heap, (-count, letter)) #negative so highest ind is first (max heap)

  while max_heap:
    count, letter = heappop(max_heap)
    for _ in range(-count):
      result.append(letter)
      
  return ''.join(result)

def main():
  print(freq_sort("Programming"))
  print(freq_sort("abcbab"))

main()