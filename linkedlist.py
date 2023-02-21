
#~^ Singly Linked List
#~# Single Node of the linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  #~! memory location


# Linked list itself
class LinkedList:
    def __init__(self):
        self.head = None  #~* Pointers
        self.tail = None  #~* Pointers

    def add_node(self, value):
        newNode = Node(value)

        #~% Is this the first time we are creating a node ??
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        #~% This is not the first time we are creating node, connect tail to newNode and the newNode will be tail itself
        else:
            self.tail.next = newNode
            self.tail = newNode

    def _print(self):
        current = self.head  #~! pointer of head node
        while current is not None:
            print(current.value)
            current = current.next  #~! Current points to next node in the memory


sll = LinkedList()
sll.add_node({"name": "Majid"})
sll.add_node({"name": "Aves"})
sll.add_node({"name": "Robinhood"})

sll._print()
