#this problem is just topological sort 

from collections import deque

def task_scheduling_order(tasks, prereqs):
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
  if len(sorted_order) != tasks:
    return []

  return sorted_order


def main():
  print("Task scheduling order: " +
        str(task_scheduling_order(3, [[0, 1], [1, 2]])))
  print("Task scheduling order: " +
        str(task_scheduling_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Task scheduling order: " +
        str(task_scheduling_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()