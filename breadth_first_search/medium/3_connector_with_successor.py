"""
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.

12
7 1
9 10 5

12 -> 7 -> 1 -> 9 -> 10 -> 5

Time Complexity: O(n)
Space Complexity: O(n)
"""


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.next = None


class Solution:
    def connect_level_order_siblings(self, root):
        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                if queue:
                    curr_node.next = queue[0]
        return root


def print_level_order(root):
    current = root
    while current:
        if current.next:
            print(str(current.val) + " -> ", end='')
        else:
            print(str(current.val))
        current = current.next


def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root = sol.connect_level_order_siblings(root)

    print("Traversal using 'next' pointer: ")
    print_level_order(root)


main()
