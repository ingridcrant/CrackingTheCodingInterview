from LinkedList import LinkedList, Node
from math import log10

def addLinkedListsReversed(node1, node2, carry_over):
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
    n.next = addLinkedListsReversed(node1.next, node2.next, curr_sum//10)
    return n

def addLinkedListsReversedStarter(linkedlist1, linkedlist2):
    sum_node = addLinkedListsReversed(linkedlist1.head, linkedlist2.head, 0)
    sum_linked_list = LinkedList()
    sum_linked_list.head = sum_node
    return sum_linked_list

# assumes that linked lists are same length
def addLinkedListsForward(node1, node2):
    if not node1.next and not node2.next:
        return Node(node1.val + node2.val)
    
    sum_node = addLinkedListsForward(node1.next, node2.next)
    ones = sum_node.val % 10
    carry = sum_node.val // 10
    sum_node.val = ones

    new_node = Node(node1.val + node2.val + carry)
    new_node.next = sum_node

    return new_node

def addLinkedListsForwardStarter(linkedlist1, linkedlist2):
    sum_node = addLinkedListsForward(linkedlist1.head, linkedlist2.head)
    sum_linked_list = LinkedList()

    if sum_node.val > 9:
        new_sum_node = Node(sum_node.val//10)
        sum_node.val = sum_node.val % 10
        new_sum_node.next = sum_node
        sum_linked_list.head = new_sum_node
    else:
        sum_linked_list.head = sum_node
    
    return sum_linked_list

def displayLinkedList(linkedlist):
    node = linkedlist.head
    while node.next:
        print(str(node.val), end="->")
        node = node.next
    print(str(node.val))

# test case
n1 = Node(9)
n1.next = Node(9)
n1.next.next = Node(9)
linkedlist1 = LinkedList()
linkedlist1.head = n1

n2 = Node(9)
n2.next = Node(9)
n2.next.next = Node(9)
linkedlist2 = LinkedList()
linkedlist2.head = n2

sumlinkedlist = addLinkedListsReversedStarter(linkedlist1, linkedlist2)
displayLinkedList(sumlinkedlist)

forwardlinkedlist = addLinkedListsForwardStarter(linkedlist1, linkedlist2)
displayLinkedList(forwardlinkedlist)