"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Time Complexity: O(n) each node is added to the queue and then later processed
Space Complexity: O(n) for the result list, also O(n) at worst for the queue becuase the largest tree level could be (n/2) + 1 
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def level_order_traversal(self, root):
        result = []

        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            curr_level = []
            for _ in range(level_size):
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(curr_level)

        return result


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(sol.level_order_traversal(root)))


main()
