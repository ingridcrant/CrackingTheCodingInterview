from LinkedList import LinkedList
from LinkedList import Node

def detectDuplicates(node, char_list):
    if not node:
        return char_list
    else:
        if node.val not in char_list:
            char_list.append(node.val)
        char_list = detectDuplicates(node.next, char_list)
        return char_list

def createLinkedList(val_list):
    if len(val_list) == 1:
        new_node = Node(val_list[0])
        return new_node
    else:
        new_node = Node(val_list[0])
        val_list = val_list[1:]
        new_node.next = createLinkedList(val_list)
        return new_node

def removeDuplicates(linkedlist):
    node = linkedlist.head
    val_list = detectDuplicates(node, [])
    linkedlist.head = createLinkedList(val_list)
    return linkedlist

# test case
linkedlist = LinkedList()
linkedlist.head = createLinkedList([char for char in "FOLLOW UP"])
new_linked_list = removeDuplicates(linkedlist)

node = new_linked_list.head
while node:
    print(node.val, end="")
    node = node.next