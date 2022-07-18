from heapq import *

def find_kth_smallest(nums, k):
  result = []
  for i in range(k):
    heappush(result, -nums[i]) #we push negative so it's a max heap
  for i in range(k, len(nums)): 
    if nums[i] < -result[0]: #if current number is smaller than the largest in our max heap, we push it
      heappop(result)
      heappush(result, -nums[i])
  return -result[0]

def main():

  print("Kth smallest number is: " +
        str(find_kth_smallest([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should 
  # be a '5'
  print("Kth smallest number is: " +
        str(find_kth_smallest([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_kth_smallest([5, 12, 11, -1, 12], 3)))


main()