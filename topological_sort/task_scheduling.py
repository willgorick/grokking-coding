#this problem is just topological sort but returning a bool for if the graph is without cycles

from collections import deque

def is_scheduling_possible(tasks, prereqs):
  sorted_order = []

  if tasks <= 0:
    return sorted_order

  #1. Initialize the graph
  in_degree = {i:0 for i in range(tasks)}
  graph = {i: []  for i in range(tasks)}

  #2. Build the graph.
  for edge in prereqs:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)
    in_degree[child] += 1

  #3. Find all sources
  sources = deque()
  for key in in_degree:
    if in_degree[key] == 0:
      sources.append(key)

  #4. For each source, add it to sorted_order and subtract '1' from all of it's children's in-degrees.  If a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sorted_order.append(vertex)
    for child in graph[vertex]:
      in_degree[child] -= 1
      if in_degree[child] == 0:
        sources.append(child)

  #topological sort not possible if graph has a cycle
  return len(sorted_order) == tasks


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()