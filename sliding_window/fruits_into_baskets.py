def fruits_into_baskets(arr):
    fruit_map = {}
    start_ind, longest_len = 0, 0
    for end_ind in range(len(arr)):
      curr_fruit = arr[end_ind]
      if curr_fruit not in fruit_map:
          fruit_map[curr_fruit] = 0
      fruit_map[curr_fruit] += 1
      while len(fruit_map) > 2:
          remove = arr[start_ind]
          fruit_map[remove] -= 1
          start_ind += 1
          if fruit_map[remove] == 0:
              del fruit_map[remove]
      longest_len = max(longest_len, end_ind-start_ind+1)
    return longest_len

def main():
  print("Maximum number of fruits: " 
           + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " 
           + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
main()
