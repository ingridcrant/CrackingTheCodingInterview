"""
Implement an algorithhm to find the kth to last element of a singly linked list
"""
from LinkedList import LinkedList
from LinkedList import Node

def createLinkedList(val_list):
    if len(val_list) == 1:
        new_node = Node(val_list[0])
        return new_node
    else:
        new_node = Node(val_list[0])
        val_list = val_list[1:]
        new_node.next = createLinkedList(val_list)
        return new_node

def findKthtoLastElement(node, element, k, current_place):
    if not node.next:
        return [element, 1]
    else:
        [element, current_place] = findKthtoLastElement(node.next, element, k, current_place)
        current_place += 1
        if current_place == k:
            element = node.val
        return [element, current_place]

def getKthtoLastElement(linkedlist, k):
    return findKthtoLastElement(linkedlist.head, None, k, 0)[0]

# test case
linkedlist = LinkedList()
linkedlist.head = createLinkedList([char for char in "THIS IS A TEST STRING"])

print(getKthtoLastElement(linkedlist, 3))