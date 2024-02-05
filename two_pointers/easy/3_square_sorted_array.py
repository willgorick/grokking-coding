"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Time Complexity: O(n) - look at each number one time at most
Space Complexity: O(1) - 3 pointers
"""
def square_sorted_array(arr):
  res = [0 for _ in arr]
  #start at the front and back of the sorted array because those will be the largest squared numbers
  l, r, res_ind = 0, len(arr)-1, len(arr)-1
  while l <= r:
    l_squared, r_squared = arr[l]*arr[l], arr[r]*arr[r]
    if l_squared > r_squared:
      res[res_ind] = l_squared
      l += 1
    else:
      res[res_ind] = r_squared
      r -= 1
    res_ind -= 1
  return res

def main():
  print("Squares: " + str(square_sorted_array([-2, -1, 0, 2, 3])))
  print("Squares: " + str(square_sorted_array([-3, -1, 0, 1, 2])))


main()