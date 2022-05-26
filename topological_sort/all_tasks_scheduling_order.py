from collections import deque

def all_orders(tasks, prereqs):
  sorted_order = []
  if tasks <= 0:
    return False

  #1. initialize the graph
  in_degree = {i: 0 for i in range(tasks)}
  graph = {i: [] for i in range(tasks)}

  #2. build the graph
  for prereq in prereqs:
    parent, child = prereq[0], prereq[1]
    graph[parent].append(child)
    in_degree[child] += 1

  #3. find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in in_degree:
    if in_degree[key] == 0:
      sources.append(key)

  print_all_topological_sorts(graph, in_degree, sources, sorted_order)

def print_all_topological_sorts(graph, in_degree, sources, sorted_order):

  if sources:
    for vertex in sources:
      sorted_order.append(vertex)
      sources_for_next_call = deque(sources) #make a copy of sources

      # only remove the current source, all others should remain in queue for the next call
      sources_for_next_call.remove(vertex)

      for child in graph[vertex]:
        in_degree[child] -= 1
        if in_degree[child] == 0:
          sources_for_next_call.append(child)

      #recursive all to print other orderings from the remaining (and new) sources
      print_all_topological_sorts(graph, in_degree, sources_for_next_call, sorted_order)

      #backtrack, remove the vertex from the sorted order and put all of its children back to consider the next sources instead of the current vertex
      sorted_order.remove(vertex)
      for child in graph[vertex]:
        in_degree[child] += 1

  # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency between tasks, or we have not processed all the tasks in this recursive call
  if len(sorted_order) == len(in_degree):
    print(sorted_order)



def main():
  print("Task Orders: ")
  all_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  all_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  all_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()