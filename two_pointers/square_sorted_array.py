def square_sorted_array(arr):
  start, end, ind = 0, len(arr)-1, len(arr)-1
  result = [0 for _ in range(len(arr))]

  while start < end:
    start_sq = arr[start]*arr[start]
    end_sq = arr[end]*arr[end]
    if start_sq > end_sq: #start from the end of our result array and add highest numbers first
      result[ind] = start_sq
      start += 1
    else:
      result[ind] = end_sq
      end -= 1
    ind -=1
  return result

def main():
  print("Squares: " + str(square_sorted_array([-2, -1, 0, 2, 3])))
  print("Squares: " + str(square_sorted_array([-3, -1, 0, 1, 2])))


main()