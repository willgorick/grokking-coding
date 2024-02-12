"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Time Complexity: O(n log n) - both the sort and the loop of heappushes are O(n log n)
Space Complexity: O(n) if the heap is full
"""

import heapq


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpuLoad = cpu_load

    def __lt__(self, other):
        return self.end < other.end


class Solution:
    def max_cpu_load(self, jobs):
        jobs.sort(key=lambda x: x.start)
        max_load = 0
        job_heap = []
        curr_load = 0
        for job in jobs:
            # while there are jobs in the heap that end before (or at the same time) that the current job starts
            while job_heap and job.start >= job_heap[0].end:
                removed_job = heapq.heappop(job_heap)
                # decrement the current load
                curr_load -= removed_job.cpuLoad
            # increment our current load
            curr_load += job.cpuLoad
            # add current job to heap
            heapq.heappush(job_heap, job)
            # update our max_load if curr_load is greater
            max_load = max(max_load, curr_load)
        return max_load


def jobify(job_list):
    jobs = []
    for job in job_list:
        jobs.append(Job(job[0], job[1], job[2]))
    return jobs


def main():
    sol = Solution()
    jobs1 = jobify([[1, 4, 3], [2, 5, 4], [7, 9, 6]])
    jobs2 = jobify([[6, 7, 10], [2, 4, 11], [8, 12, 15]])
    jobs3 = jobify([[1, 4, 2], [2, 4, 1], [3, 6, 5]])
    print(sol.max_cpu_load(jobs1))
    print(sol.max_cpu_load(jobs2))
    print(sol.max_cpu_load(jobs3))


main()
