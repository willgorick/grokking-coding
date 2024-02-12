"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Time Complexity: O(n) each interval is considered once
Space Complexity: O(n) if there are no overlaps the output list will be of size N

"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:
    def insert_interval(self, intervals, insert):
        result = []

        i = 0
        # any interval ending before the inserted interval's start can be left as is
        while i < len(intervals) and intervals[i].end < insert.start:
            result.append(intervals[i])
            i += 1

        # merge any intervals that overlap with the insert interval (don't end before this interval starts and start before this interval ends)
        while i < len(intervals) and intervals[i].start <= insert.end:
            insert.start = min(insert.start, intervals[i].start)
            insert.end = max(insert.end, intervals[i].end)
            i += 1

        result.append(insert)
        # any interval starting after the inserted interval's end can be left as is
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


def main():
    sol = Solution()
    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    print("Intervals after inserting the new interval: ", end="")
    for i in (sol.insert_interval(intervals, Interval(4, 6))):
        i.print_interval()
    print()

    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    print("Intervals after inserting the new interval: ", end="")
    for i in (sol.insert_interval(intervals, Interval(4, 10))):
        i.print_interval()
    print()

    intervals = [Interval(2, 3), Interval(5, 7)]
    print("Intervals after inserting the new interval: ", end="")
    for i in (sol.insert_interval(intervals, Interval(1, 4))):
        i.print_interval()
    print()


main()
