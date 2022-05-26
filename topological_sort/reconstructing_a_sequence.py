from collections import deque

def can_construct(original, seqs):
  sorted_order = []
  if len(original) <= 0:
    return False

  #1. initialize graph  
  in_degree = {}
  graph = {}

  for seq in seqs:
    for num in seq:
      in_degree[num] = 0
      graph[num] = []

  #2. build graph
  for seq in seqs:
    for i in range(1, len(seq)):
      parent, child = seq[i-1], seq[i]
      graph[parent].append(child)
      in_degree[child] += 1

  #if we don't have ordering rules for all numbers we won't be able to construct the sequence
  if len(in_degree) != len(original):
    return False

  #3 identify sources
  sources = deque()
  for key in in_degree:
    if in_degree[key] == 0:
      sources.append(key)

  #4. go through sources and decrement their children's in_degrees
  while sources:
    if len(sources) > 1:
      return False #more than one source menas there are more ways than one to reconstruct
    if original[len(sorted_order)] != sources[0]:
      return False #next source/number is different from the original sequence
    
    vertex = sources.popleft()
    sorted_order.append(vertex)
    for child in graph[vertex]:
      in_degree[child] -= 1
      if in_degree[child] == 0:
        sources.append(child)

  return len(sorted_order) == len(original)


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))

main()