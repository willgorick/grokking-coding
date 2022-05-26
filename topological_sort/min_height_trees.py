from collections import deque

#because this is undirected, any leaf will not give us an MHT, b/c whatever node the leaf leads to will always have a height one less
# a -> b, b->c, b->d.  a won't be the root of MHT because b will always have one less height as MHT: b->a, b->c, b->d

def find_trees(nodes, edges):
  if nodes <= 0:
    return []
  
  #with only one node, the in-degree will be 0, so we handle it beforehand
  if nodes == 1:
    return 0

  #1 initialize graph
  in_degree = {i: 0 for i in range(nodes)}
  graph = {i: [] for i in range(nodes)}

  #2 build graph
  for edge in edges:
    n1, n2 = edge[0], edge[1]
    #since undirected, add link in both directions
    graph[n1].append(n2)
    graph[n2].append(n1)
    in_degree[n1] += 1
    in_degree[n2] += 1

  #3 find sources
  leaves = deque()
  for key in in_degree:
    if in_degree[key] == 1:
      leaves.append(key)

  #4 Remove leaves level by level and subtract each leave's child's in-degrees.  Repeat until we only have 1 or 2 nodes, which will be our answer.  Any node that has already beena leaf can't be the root of the min height tree, because its adjacent non-leaf node will always be a better candidate.  The last 1 or 2 remaining "leaves" had the most connections to other nodes and are the roots of our MHTs
  total_nodes = nodes
  while total_nodes > 2:
    leaves_size = len(leaves)
    total_nodes -= leaves_size
    for i in range(leaves_size):
      vertex = leaves.popleft()
      for child in graph[vertex]:
        in_degree[child] -= 1
        if in_degree[child] == 1:
          leaves.append(child)
  return list(leaves)

def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))
main()