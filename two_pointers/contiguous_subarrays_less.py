from collections import deque

def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)): #if we ever get over the product, divide out the leftmost digit and move the left pointer
      product /= arr[left]
      left += 1
    temp_list = deque()
    for i in range(right, left-1, -1): #for each element between right and left, add a list with first one, then two, etc. 
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
      
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))

main()