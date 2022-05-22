class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_paths(root, goal):
  return recursive_count_paths(root, goal, [])

def recursive_count_paths(node, goal, curr_path):
  if node is None:
    return 0

  curr_path.append(node.val) ## add curr_node to path 
  path_count, path_sum = 0, 0

  for i in range(len(curr_path)-1, -1, -1): #find sum of all subpaths in current path list
    path_sum += curr_path[i]
    if path_sum == goal:
      path_count += 1

  #traverse left subtree
  path_count += recursive_count_paths(node.left, goal, curr_path) 

  #traverse right subtree
  path_count += recursive_count_paths(node.right, goal, curr_path)

  #remove node to backtrack
  del curr_path[-1]

  return path_count

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()

