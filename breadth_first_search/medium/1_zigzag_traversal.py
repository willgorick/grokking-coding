"""
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

Time Complexity: O(n)
Space Complexity: O(n)
"""


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def zigzag_traversal(self, root):
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)
        r2l = True
        while queue:
            level_size = len(queue)
            curr_level = deque()
            for _ in range(level_size):
                curr_node = queue.popleft()
                if r2l:
                    curr_level.appendleft(curr_node.val)
                else:
                    curr_level.append(curr_node.val)
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)
            result.append(list(curr_level))
            r2l = not r2l
        return result


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print(sol.zigzag_traversal(root))


main()
