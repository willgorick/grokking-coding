from heapq import *
import numbers

class Element:
  def __init__(self, number, frequency, sequence):
    self.number = number
    self.frequency = frequency
    self.sequence = sequence

  def __lt__(self, other): #this makes the heap handle sorting by recency/frequcney for us
    #higher freq wins
    if self.frequency != other.frequency:
      return self.frequency > other.frequency #using > here in lt, makes the heap sort for us
    # if same freq, return whichever was pushed later
    return self.sequence > other.sequence

class Stack:
  def __init__(self):
    self.heap = []
    self.freq_map = {}
    self.sequence = 0

  def push(self, num):
    self.freq_map[num] = self.freq_map.get(num, 0) + 1
    heappush(self.heap, Element(num, self.freq_map[num], self.sequence))
    self.sequence += 1

  def pop(self):
    num = heappop(self.heap).number
    if self.freq_map[num] > 1:
      self.freq_map[num] -= 1
    else:
      del self.freq_map[num]

    return num

def main():
  frequencyStack = Stack()
  frequencyStack.push(1)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()