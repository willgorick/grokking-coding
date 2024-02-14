"""
Given the head of a LinkedList and a number 'k', reverse every 'k' sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse_every_k_element_sublist(self, head, k):
        if k <= 1 or not head:
            return head
        curr = head
        previous = None

        while curr:
            last_node_of_previous_part = previous
            # after reversing, the current node will be the last one of the sublist
            last_node_of_current_part = curr

            i = k
            while curr and i > 0:
                next = curr.next
                curr.next = previous
                previous = curr
                curr = next
                i -= 1

            # connect to the previous part if there was one
            if last_node_of_previous_part is not None:
                last_node_of_previous_part.next = previous
            # if there wasn't a previous part then we just started our loop, so we set the head to previous (the new start of the reversed list)
            else:
                head = previous

            # connect the last node of the current part to curr (which is the start of the next part)
            last_node_of_current_part.next = curr
            # set the previous to be the last node of the current list
            previous = last_node_of_current_part

        return head


def print_list(head):
    temp = head
    while temp is not None:
        if temp.next:
            print(temp.val, end=" -> ")
        else:
            print(temp.val)
        temp = temp.next


def main():
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    print_list(head)

    result = sol.reverse_every_k_element_sublist(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    print_list(result)


main()
