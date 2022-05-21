from heapq import *

class Meeting:
  def __init__(self, start, end):
   self.start = start
   self.end = end

  def __lt__(self, other):
    return self.end < other.end
  

def min_rooms(meetings):
  meetings.sort(key=lambda x: x.start)
  min_rooms = 0
  min_heap = []

  for meeting in meetings:
    while(len(min_heap) > 0 and meeting.start >= min_heap[0].end): #while there are meeting in the heap that end before ours starts, remove them
      heappop(min_heap)
    heappush(min_heap, meeting) #add our meeting to the heap
    min_rooms = max(min_rooms, len(min_heap))
  return min_rooms

def main():
  print("Minimum meeting rooms required: " +
        str(min_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))

main()