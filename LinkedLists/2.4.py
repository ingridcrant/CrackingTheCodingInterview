"""
Write code to partition a linked list around a value x, such that all nodes less than 
x come before all nodes greater than or equal to x.
"""
from LinkedList import LinkedList
from LinkedList import Node

def partitionlinkedlist(val_list, current_node, node_x):
    if not current_node:
        return val_list
    else:
        if current_node != node_x:
            if current_node.val >= node_x.val:
                val_list.append(current_node.val)
            else:
                val_list = [current_node.val] + val_list
        val_list = partitionlinkedlist(val_list, current_node.next, node_x)
        current_node.val = val_list[-1]
        return val_list[:(-1)]

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

print("After reordering:", end=" ")
partitionlinkedlist([mid.val], linkedlist.head, mid)
displayLinkedList(linkedlist)