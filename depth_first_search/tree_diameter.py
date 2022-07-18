
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class TreeDiameter:
  def __init__(self):
    self.tree_diameter = 0

  def find_diameter(self, root): #the longest path between any two leaves
    self.calculate_height(root)
    return self.tree_diameter

  def calculate_height(self, node):
    if node is None:
      return 0

    left_tree_height = self.calculate_height(node.left)
    right_tree_height = self.calculate_height(node.right)

    #only need to update our max_diameter so far if we're at a node with left and right children
    if left_tree_height is not None and right_tree_height is not None:

      #the diameter is equal to the height of the left subtree + the right subtree + 1
      diameter = left_tree_height + right_tree_height + 1

      #update the global tree diameter
      self.tree_diameter = max(self.tree_diameter, diameter)
    
    #height of the current node will be equal to the max of the heights of left/right + 1 for the current node
    return max(left_tree_height, right_tree_height) + 1

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()