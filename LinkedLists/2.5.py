from LinkedList import LinkedList, Node
from math import log10

def addLinkedLists(node1, node2, carry_over):
    if not node1 and not node2:
        if carry_over == 0:
            return None
        else:
            return Node(carry_over)
    elif node1 and not node2:
        curr_sum = node1.val + carry_over
    elif not node1 and node2:
        curr_sum = node2.val + carry_over
    else:
        curr_sum = node1.val + node2.val + carry_over
    n = Node(curr_sum % 10)
    n.next = addLinkedLists(node1.next, node2.next, curr_sum//10)
    return n

def displayLinkedList(linkedlist):
    node = linkedlist.head
    while node.next:
        print(str(node.val), end="->")
        node = node.next
    print(str(node.val))

# test case
n1 = Node(7)
n1.next = Node(1)
n1.next.next = Node(6)
linkedlist1 = LinkedList()
linkedlist1.head = n1

n2 = Node(5)
n2.next = Node(9)
n2.next.next = Node(2)
linkedlist2 = LinkedList()
linkedlist2.head = n2

sumlinkedlist = LinkedList()
sumlinkedlist.head = addLinkedLists(linkedlist1.head, linkedlist2.head, 0)
displayLinkedList(sumlinkedlist)