"""
For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

Time Complexity: O(n log k) where k is the number of employees.  This is because our heap will only ever have at most one interval from each employee, meaning the insert time is log k.  Iterating through each interval forms the n part of our O(n log k) complexity.
Space Complexity: O(k) space for the heap, but the result list could theoretically have O(n-1) intervals if there is a gap between every single interval for all employees.
"""

from heapq import heappush, heappop


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        # index of the interval in the employee list
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        # min heap based on meeting.start
        return self.interval.start < other.interval.start


class Solution:
    def find_free_time(self, schedule):
        if not schedule:
            return []

        result, min_heap = [], []
        # insert the first interval for each employee into the heap
        for i in range(len(schedule)):
            heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

        # keep track of previous end for finding free time blocks
        previous_end = min_heap[0].interval.end
        while min_heap:
            # current employee interval
            curr_employee_interval = heappop(min_heap)
            # index of this employee in the schedule
            curr_employee_index = curr_employee_interval.employeeIndex
            # index of this interval in the employee's schedule
            curr_interval_index = curr_employee_interval.intervalIndex

            # if there is a gap between previous end and current start, add it to our result list and then update the previous end to be the current interval's end
            if previous_end < curr_employee_interval.interval.start:
                result.append(
                    Interval(previous_end, curr_employee_interval.interval.start))
                previous_end = curr_employee_interval.interval.end

            # if there's no gap between them, but the current interval ends after the previous, update our previous value to reflect the later end time
            elif previous_end < curr_employee_interval.interval.end:
                previous_end = curr_employee_interval.interval.end

            curr_employees_schedule = schedule[curr_employee_index]
            # if the current employee has more intervals we haven't looked at
            if len(curr_employees_schedule) > curr_interval_index+1:
                # add the next interval for this employee to our heap (will be sorted by start time)
                heappush(min_heap, EmployeeInterval(
                    curr_employees_schedule[curr_interval_index+1], curr_employee_index, curr_interval_index+1))

        return result


def print_interval(i):
    print("[" + str(i.start) + ", " + str(i.end) + "]", end='')


def main():
    sol = Solution()
    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in sol.find_free_time(input):
        print_interval(interval)
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in sol.find_free_time(input):
        print_interval(interval)
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in sol.find_free_time(input):
        print_interval(interval)
    print()


main()
