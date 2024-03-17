"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.


Time Complexity: O(n) 
Space Complexity: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def min_depth(self, root):
        min_depth = 0
        if not root:
            return min_depth
        queue = deque()
        queue.append(root)

        while queue:
            min_depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if not (curr_node.left or curr_node.right):
                    return min_depth
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return min_depth

    def max_depth(self, root):
        max_depth = 0
        if not root:
            return max_depth
        queue = deque()
        queue.append(root)

        while queue:
            max_depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return max_depth


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(13)
    print("Min depth: " + str(sol.min_depth(root)))
    print("Max depth: " + str(sol.max_depth(root)))


main()
