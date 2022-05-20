
def cycle_exists(arr):
  for i in range(len(arr)):
    is_forward = arr[i] >= 0
    slow, fast = i, i

    while True:
      slow = find_next_ind(arr, is_forward, slow)
      fast = find_next_ind(arr, is_forward, fast)
      if (fast != -1): #if fast is valid, take another step
        fast = find_next_ind(arr, is_forward, fast)
      if slow == -1 or fast == -1 or slow == fast:
        break
    if slow != -1 and slow == fast: #implies fast != -1
      return True
  return False #haven't found a cyle starting at any element


def find_next_ind(arr, is_forward, curr_ind):
  direction = arr[curr_ind] >= 0
  if is_forward != direction:
    return -1
  next_ind = (curr_ind + arr[curr_ind]) % len(arr)

  if next_ind == curr_ind: #one element cycle, we don't want this
    return -1

  return next_ind


def main():
  print(cycle_exists([1, 2, -1, 2, 2]))
  print(cycle_exists([2, 2, -1, 2]))
  print(cycle_exists([2, 1, -1, -2]))

main()