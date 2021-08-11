"""
Implement an algorithm to delete a node in the middle of a signly linked list, 
given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e
"""
from LinkedList import LinkedList
from LinkedList import Node

def deletemiddle(node):
    if not node.next:
        # can't delete the end of a linked list
        return
    else:
        node.val = node.next.val
        node.next = node.next.next

def displayLinkedList(linkedlist):
    node = linkedlist.head
    while node.next:
        print(str(node.val), end="->")
        node = node.next
    print(str(node.val))


# test case
n = Node(1)
n.next = Node(2)
n.next.next = Node(8)
n.next.next.next = Node(3)

mid = Node(7)
n.next.next.next.next = mid
n.next.next.next.next.next = Node(0)
n.next.next.next.next.next.next = Node(4)
print("Original List:", end=" ")
linkedlist = LinkedList()
linkedlist.head = n
displayLinkedList(linkedlist)

print("After deleting mid node:", end=" ")
deletemiddle(mid)
displayLinkedList(linkedlist)