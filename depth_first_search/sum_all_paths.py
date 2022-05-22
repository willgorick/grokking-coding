class TreeNode:
  def __init__(self, val, left=None, right=None, sum=0):
    self.val = val
    self.left = left
    self.right = right
    self.sum = sum


def sum_of_all(node):
  if not node:
    return
  return sub_sum(node, 0)

def sub_sum(node, sum_path):
  if node is None:
    return 0

  curr_sum = node.val
  sum_path = sum_path*10 + curr_sum
  if node.left is None and node.right is None:
    return sum_path
  return sub_sum(node.left, sum_path) + sub_sum(node.right, sum_path)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(sum_of_all(root)))

  root = TreeNode(1)
  root.left = TreeNode(7)
  root.right = TreeNode(9)
  root.right.left = TreeNode(2)
  root.right.right = TreeNode(9)
  print("Total Sum of Path Numbers: " + str(sum_of_all(root)))



main()