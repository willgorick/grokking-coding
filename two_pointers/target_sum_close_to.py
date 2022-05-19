import math

def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_diff = math.inf
  for i in range(len(arr)-2):
    left = i + 1
    right = len(arr) - 1
    while (left < right):
      target_diff = target_sum - arr[i] - arr[left] - arr[right]
      if target_diff == 0:
        return target_sum
      
      if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff): #part after or is b/c if target_diff is larger that means our sum is less than the target_sum
        smallest_diff = target_diff
      if target_diff > 0:
        left += 1
      else:
        right -= 1
  return target_sum - smallest_diff 

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()