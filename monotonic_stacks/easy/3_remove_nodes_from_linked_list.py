"""
Given the head node of a singly linked list, modify the list such that any node that has a node with a greater value to its right gets removed. The function should return the head of the modified list.

Time Complexity: O(n), 2n again
Space Complexity: O(n) stack or the output linkedlist could be O(n)
"""


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def remove_nodes(self, head):
        stack = []
        curr = head
        while curr:
            # if current value is greater then we need to remove the previous value
            while stack and stack[-1].val < curr.val:
                stack.pop()
            # re-link the now previous value in the list with curr
            if stack:
                stack[-1].next = curr
            # add curr to the stack then move onto the next one
            stack.append(curr)
            curr = curr.next
        return stack[0]


def main():
    sol = Solution()

    # Creating the linked list 5 -> 3 -> 7 -> 4 -> 2 -> 1
    head1 = Node(5)
    head1.next = Node(3)
    head1.next.next = Node(7)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(2)
    head1.next.next.next.next.next = Node(1)
    head1 = sol.remove_nodes(head1)

    # Printing the modified list: 7 -> 4 -> 2 -> 1
    node = head1
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

    head2 = Node(5)
    head2.next = Node(4)
    head2.next.next = Node(5)
    head2.next.next.next = Node(4)
    head2.next.next.next.next = Node(5)
    head2 = sol.remove_nodes(head2)
    node = head2
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next


main()
