
from collections import deque
from pydoc import source_synopsis

def find_order(words):
  if len(words) == 0:
    return ""

  #1. initialize graph
  in_degree = {}
  graph = {}
  for word in words: 
    for char in word:
      in_degree[char] = 0
      graph[char] = []


  #2. build the graph
  for i in range(0, len(words)-1):
    w1, w2 = words[i], words[i+1]
    for j in range(min(len(w1), len(w2))):
       parent, child = w1[j], w2[j]
       #w1 before w2 so it's the parent
       if parent != child: #if the two chars are different
         graph[parent].append(child)
         in_degree[child] += 1
         break #only the first diff character between two words helps us

  #3. Find all sources
  sources = deque()
  print(in_degree)
  print(graph)
  for key in in_degree:
    if in_degree[key] == 0:
      sources.append(key)

  #4. For each source, add it to the sorted_order an subtract one from all of it's children's in-degrees.  If a child's in-degree becomes zero, add it to the source queue
  sorted_order = []
  while sources:
    vertex = sources.popleft() #the order works b/c the dictionary is already lexicographically sorted
    sorted_order.append(vertex)
    for child in graph[vertex]:
      in_degree[child] -= 1
      if in_degree[child] == 0:
        sources.append(child)
  
  if len(sorted_order) != len(in_degree):
    return ""

  return "".join(sorted_order)


def main():
  # print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  # print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()

