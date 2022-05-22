class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def all_paths(root, goal):
  all_paths = []
  dfs(root, goal, [], all_paths)
  return all_paths

def dfs(curr_node, goal, curr_path, all_paths):
  if curr_node is None:
    return
    
  curr_path.append(curr_node.val)

  if curr_node.val == goal and curr_node.left is None and curr_node.right is None:
    all_paths.append(list(curr_path))
  else: 
    dfs(curr_node.left, goal-curr_node.val, curr_path, all_paths) 
    dfs(curr_node.right, goal-curr_node.val, curr_path, all_paths)
  
  del curr_path[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": ")
  for path in all_paths(root, required_sum):
    for i, node in enumerate(path):
      if i < len(path)-1:
        print(node, end=" -> ")
      else:
        print(node, end="\n")


main()