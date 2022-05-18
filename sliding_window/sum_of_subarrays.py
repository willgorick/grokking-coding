def max_sum_of_subarray(K, arr):
  result = 0
  curr_sum, start_ind = 0, 0
  for end_ind in range(len(arr)):
      curr_sum += arr[end_ind]
      if end_ind >= K-1:
        if curr_sum > result:
          result = curr_sum
        curr_sum -= arr[start_ind]
        start_ind += 1
  return result

def main():
  print("Maximum sum of a subarray of size K: " +
      str(max_sum_of_subarray(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + 
      str(max_sum_of_subarray(2, [2, 3, 4, 1, 5])))

main()
