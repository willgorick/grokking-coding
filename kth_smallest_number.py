#lots of different ways to solve this problem
import math
from heapq import *
import random 

def find_Kth_smallest_number(nums, k):
  # return brute_force(nums, k)
  # return brute_force_sorted(nums, k)
  # return max_heap(nums, k)
  # return quicksort(nums, k, 0, len(nums)-1)
  return median_of_medians_sort(nums, k, 0, len(nums)-1)


def median_of_medians_sort(nums, k, start, end):
  p = median_of_medians_partition(nums, start, end)

  if p == k-1:
    return nums[p]

  if p > k-1: 
    return median_of_medians_sort(nums, k, start, p-1)
  
  return median_of_medians_sort(nums, k, p+1, end)

def median_of_medians_partition(nums, low, high):
  if low == high:
    return low

  median = median_of_medians(nums, low, high)

  #find median in the array and swap it with nums[high], which will become our pivot
  for i in range(low, high):
    if nums[i] == median:
      nums[i], nums[high] = nums[high], nums[i]
      break

  pivot = nums[high]
  for i in range(low, high):
    #all elements less than 'pivot' will be before index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  #put pivot in the correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low

def median_of_medians(nums, low, high):
  n = high - low + 1

  #if less than 5 elems, ignore partitioning algo
  if n < 5:
    return nums[low]

  #partition the array into chunks of 5
  partitions = [nums[j:j+5] for j in range(low, high+1, 5)] #how does this not go out of bounds

  #ignore any partition with less than 5 elements
  full_partitions = [partition for partition in partitions if len(partition) == 5]

  sorted_partitions = [sorted(partition) for partition in full_partitions]

  medians = [partition[2] for partition in sorted_partitions]

  return median_of_medians_partition(medians, 0, len(medians)-1)

def quicksort(nums, k, start, end):
  p = partition(nums, k, start, end)
  if p == k - 1:
    return nums[p]
  if p > k - 1: #search lower part
    return quicksort(nums, k, start, p-1)
  
  #search higher part
  return quicksort(nums, k, p+1, end)

def partition(nums, k, low, high):
  if low == high:
    return low
  
  #randomized pivot makes worst case significantly less likely
  pivotIndex = random.randint(low, high)
  nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]

  pivot = nums[high]
  for i in range(low, high):
    if nums[i] < pivot:
      #all elements less than 'pivot' must be before the index 'low'
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  #put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low

def max_heap(nums, k):
  max_heap = []
  n = len(nums)
  if n < k:
    return False

  for i in range(k):
    heappush(max_heap, -nums[i])
  
  for i in range(k, len(nums)):
    if -nums[i] > max_heap[0]:
      heappop(max_heap)
      heappush(max_heap, -nums[i])

  return -max_heap[0]

def brute_force_sorted(nums, k):
  return sorted(nums)[k-1]

def brute_force(nums, k):
  prev_smallest_num, prev_smallest_ind = -math.inf, -1
  curr_smallest_num, curr_smallest_ind = math.inf, -1

  for i in range(k):
    for j in range(len(nums)):
      #greater than previous smallest number, less than current
      if nums[j] > prev_smallest_num and nums[j] < curr_smallest_num:
        #found the next smallest number
        curr_smallest_num = nums[j]
        curr_smallest_ind = j
      elif nums[j] == prev_smallest_num and j > prev_smallest_ind:
        #found a number equal to the prev smallest; since numbers can repeat, we will consider nums[j] only if it has a different index
        curr_smallest_num = nums[j]
        curr_smallest_ind = j
        break #break here b/c we've found our definitive smallest number
    prev_smallest_num = curr_smallest_num
    prev_smallest_ind = curr_smallest_ind
    curr_smallest_num = math.inf
  
  return prev_smallest_num

def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))
  # as there're two 5s in input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))

main()