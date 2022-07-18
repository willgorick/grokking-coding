
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def dfs(root, goal):
  if root is None:
    return False
  if root.val == goal and root.left is None and root.right is None:
    return True
  new_goal = goal-root.val
  return dfs(root.left, new_goal) or dfs(root.right, new_goal)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(dfs(root, 23)))
  print("Tree has path: " + str(dfs(root, 16)))

main()