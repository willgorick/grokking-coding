def conflicting(arr):
  if len(arr) < 2:
    return True
  arr.sort(key=lambda x: x[0])
  end = arr[0][1]
  for i in range(1, len(arr)):
    if arr[i][0] <= end: #if current element starts before prev ends
      return False
    end = arr[i][1]
  return True
    
def find_conflicts(arr):
  results = []
  if len(arr) < 2:
    return True
  arr.sort(key=lambda x: x[0])
  start = arr[0][0]
  end = arr[0][1]
  for i in range(1, len(arr)):
    if arr[i][0] < end: #if current element starts before prev ends
      results.append([[start,end], arr[i]])
      end = max(end, arr[i][1]) #set the new start/end to be the whole overlapping interval
      start = min(start, arr[i][0])
    else: 
      end = arr[i][1]
      start = arr[i][0]
  return results

def main():
  print("Can attend all appointments: " + 
            str(conflicting([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + 
            str(conflicting([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + 
            str(conflicting([[4, 5], [2, 3], [3, 6]])))

  print(find_conflicts([[4, 5], [2, 3], [3, 6], [5,7], [7,8]]))
main()
  