"""
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Time Complexity: O(n log n) for sorting, as well as each heappush taking O(log n) meaning if all meetings overlapped we would N logN operations
Space Complexity: O(n) for sorting as well as for the heap if all meetings overlap
"""

import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        #sort meetings by their end times, min heap will put the lowest (aka soonest) end times first
        return self.end < other.end

class Solution:
    def minimum_rooms(self, intervals):
        intervals.sort(key=lambda x: x.start)
        min_rooms = 0
        min_heap = []
        for meeting in intervals:
            #remove all meetings that have ended (meaining their room is now free)
            while min_heap and meeting.start >= min_heap[0].end:
                heapq.heappop(min_heap)
            #add the current message to our heap
            heapq.heappush(min_heap, meeting)
            #update the result if we now have more meetings in progress than our previous max
            min_rooms = max(min_rooms, len(min_heap))
        
        return min_rooms

def intervalify(arr):
    intervals = []
    for pair in arr:
        intervals.append(Interval(pair[0], pair[1]))
    return intervals

def main():
    sol = Solution()
    intervals1 = intervalify([[1,4], [2,5], [7,9]])
    intervals2 = intervalify([[6,7], [2,4], [8,12]])
    intervals3 = intervalify([[1,4], [2,3], [3,6]])
    intervals4 = intervalify([[4,5], [2,3], [2,4], [3,5]])
    print(sol.minimum_rooms(intervals1))
    print(sol.minimum_rooms(intervals2))
    print(sol.minimum_rooms(intervals3))
    print(sol.minimum_rooms(intervals4))

main()