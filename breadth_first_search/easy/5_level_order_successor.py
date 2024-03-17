"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.


Time Complexity: O(n), loop through each node
Space Complexity: O(n) for the queue containing potentially N/2
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def level_order_succesor(self, root, key):
        queue = deque()
        if not root:
            return None

        queue.append(root)
        next = False
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if next:
                    return curr_node
                if curr_node.val == key:
                    next = True
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return None


def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = sol.level_order_succesor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = sol.level_order_succesor(root, 9)
    if result:
        print(result.val)

    result = sol.level_order_succesor(root, 12)
    if result:
        print(result.val)


main()
