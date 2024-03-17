"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

Time Complexity: O(n) each node is added to the queue and then processed later
Space Complexity: O(n) for the result list, also O(n/2) == O(n) for the queue
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def reverse_level_order_traversal(self, root):
        result = deque()
        if not root:
            return result
        queue = deque()
        queue.append(root)

        while queue:
            level_len = len(queue)
            curr_level = []
            for _ in range(level_len):
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.appendleft(curr_level)
        return list(result)


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " +
          str(sol.reverse_level_order_traversal(root)))


main()
