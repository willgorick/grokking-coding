import math

class ArrayReader:
  def __init__(self, arr):
    self.arr = arr

  def get(self, ind):
    if ind >= len(self.arr):
      return math.inf
    return self.arr[ind]

def search_infinite_array(reader, key):
  start, end  = 0, 1
  while reader.get(end) < key:
    new_start = end +1
    end += (end - start + 1) * 2
    start = new_start
  while start <= end:
    mid = (start + end) // 2
    if reader.get(mid) == key:
      return mid
    if reader.get(mid) > key:
      end = mid - 1
    else:
      start = mid + 1
  return -1

def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_infinite_array(reader, 16))
  print(search_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_infinite_array(reader, 15))
  print(search_infinite_array(reader, 200))


main()
