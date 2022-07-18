#source: a node with no incoming edge, only outgoing
#sink: a node with only incoming edges, no outgoing
# topological ordering is only possible when the graph has no direct cycles

from collections import deque

def topological_sort(vertices, edges):
  sorted_order = []

  if vertices <= 0:
    return sorted_order

  #1. Initialize the graph
  in_degree = {i:0 for i in range(vertices)}
  graph = {i: []  for i in range(vertices)}

  #2. Build the graph.
  for edge in edges:
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
  #if we want to determine if a graph has a cycle we can return a bool at this point
  if len(sorted_order) != vertices:
    return []

  return sorted_order


def main():
  # print("Topological sort: " +
  #       str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  # print("Topological sort: " +
  #       str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  # print("Topological sort: " +
  #       str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], \
  #              [3, 0], [3, 1], [3, 2], [4, 1]])))
main()