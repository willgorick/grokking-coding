from heapq import *

def rearrange(string):
  char_freq, max_heap = {}, []
  for x in string:
    char_freq[x] = char_freq.get(x, 0) + 1
  
  for char, freq in char_freq.items():
    heappush(max_heap, (-freq, char))
  
  prev_char, prev_freq = None, 0
  result = []
  while max_heap:
    freq, char = heappop(max_heap)
    # add back the previous char if it's frequency is still greater than 0
    if prev_char and -prev_freq > 0:
      heappush(max_heap, (prev_freq, prev_char))
    # append current character to string and decrement its count
    result.append(char)
    prev_char = char
    prev_freq = freq+1 #decrement by 1 (freaking negatives)
  
  return ''.join(result) if len(result) == len(string) else False


def main():
  print(rearrange("aappp"))
  print(rearrange("Programming"))
  print(rearrange("aapa"))

main()