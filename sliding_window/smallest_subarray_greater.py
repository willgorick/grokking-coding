import sys


#Attempt one
def smallest_subarray_greater(S, arr):
  min_len = sys.maxint
  start_ind, end_ind, curr_sum = 0, 0, 0
  shrink = False
  while end_ind < len(arr):
    if arr[end_ind] > S:
      return 1
    if not shrink:
      curr_sum += arr[end_ind]
      shrink = False
    if curr_sum > S:
      if end_ind - start_ind < min_len:
        min_len = end_ind - start_ind
      curr_sum -= arr[start_ind]
      shrink = True
      start_ind += 1
    else:
      end_ind += 1
  return min_len

#Attempt 2
def smallest_subarray_greater2(S, arr):
  curr_sum = 0
  min_length = sys.maxint
  start_ind = 0

  for end_ind in range(0, len(arr)):
    curr_sum += arr[end_ind]
    while curr_sum >= S:
      min_length = min(min_length, end_ind - start_ind + 1)
      curr_sum -= arr[start_ind]
      start_ind += 1
  if min_length == sys.maxint:
    return 0
  return min_length


def main():
  print("Smallest subarray length: " 
     + str(smallest_subarray_greater(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " 
     + str(smallest_subarray_greater(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " 
     + str(smallest_subarray_greater(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " 
     + str(smallest_subarray_greater2(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " 
     + str(smallest_subarray_greater2(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " 
     + str(smallest_subarray_greater2(8, [3, 4, 1, 1, 6])))

main()