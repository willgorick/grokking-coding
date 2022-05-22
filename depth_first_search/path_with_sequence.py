class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_path(root, sequence):
  if not root:
    return len(sequence) == 0
  return find_path_recursive(root, sequence, 0)

def find_path_recursive(curr_node, sequence, seq_ind):
  if curr_node is None:
    return False
  seq_len = len(sequence)
  if seq_ind >= seq_len or curr_node.val != sequence[seq_ind]:
    return False
  
  if curr_node.left is None and curr_node.right is None and seq_ind == seq_len -1:
    return True

  return find_path_recursive(curr_node.left, sequence, seq_ind +1) or find_path_recursive(curr_node.right, sequence, seq_ind +1)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))

main()