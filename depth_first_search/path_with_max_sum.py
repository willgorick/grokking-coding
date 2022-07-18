
import math
from turtle import right

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class MaxPathSum:
  def find_max_path_sum(self, root):
    self.global_max_sum = -math.inf
    self.find_max_path_sum_recursive(root)
    return self.global_max_sum

  def find_max_path_sum_recursive(self, node):
    if node is None:
      return 0
      
    max_path_sum_left = self.find_max_path_sum_recursive(node.left)
    max_path_sum_right = self.find_max_path_sum_recursive(node.right)

    max_path_sum_left = max(max_path_sum_left, 0) #if the max_path_sum for one side is negative, we just won't include it in our calculation
    max_path_sum_right = max(max_path_sum_right, 0)

    local_max_sum = max_path_sum_left + max_path_sum_right + node.val

    self.global_max_sum = max(self.global_max_sum, local_max_sum) #try to set global max with this node as the root of the path

    return max(max_path_sum_left, max_path_sum_right) + node.val #only return the max of the left or right (plus current node value)

def main():
  maximumPathSum = MaxPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_max_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_max_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_max_path_sum(root)))

main()