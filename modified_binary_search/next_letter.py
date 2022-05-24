
def next_letter(letters, key):
  n = len(letters)-1
  if key > letters[n]: #wrap around
    return letters[0]
  start, end = 0, n
  while start <= end:
    mid = (start + end) // 2
    if key == letters[mid]:
      return letters[(mid+1) % (n+1)]
    if key < letters[mid]:
      end = mid - 1
    else:
      start = mid + 1
  return letters[start % (n+1)]

def main():
  print(next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(next_letter(['a', 'c', 'f', 'h'], 'm'))
  print(next_letter(['a', 'c', 'f', 'h'], 'h'))



main()
