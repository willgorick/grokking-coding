def num_triplets_below(arr, target):
  trip_count = 0
  arr.sort()
  for i in range(len(arr)-2): #-1 would be the last index, so -2 because our end pointer handles the last index
    trip_count += search_pair(arr, target-arr[i], i) #target-arr[i] is the number our other two numbers need to add up to less than in order for this to be a valid triplet
  return trip_count

def search_pair(arr, target_sum, ind):
  count = 0
  left, right = ind+1, len(arr)-1
  while left < right:
    curr_sum = arr[left] + arr[right]
    if curr_sum < target_sum:
      #arr[right] is > arr[left] so if arr[left] + any number between arr[right] and arr[left] will also be less than the sum
      count += right-left 
      #0,1,4(0,1,3)(0,1,2)
      # 3
      # 0,2,4(0,2,3)
      # 2
      
      left += 1
    else:
      right -= 1
  return count

def main():
  print(num_triplets_below([-1, 0, 2, 3], 3))
  print(num_triplets_below([-1, 4, 2, 1, 3], 5))

main()