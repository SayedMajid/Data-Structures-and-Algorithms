# ~^ Doubly Linked List
# ~# Single node of linked list


class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # ~* Pointers
        self.tail = None  # ~* Pointers

    def add_node(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode  # ~^ assigning prev node next to newNode
            newNode.prev = (
                self.tail
            )  # ~^ assigning current node's previous pointer to previous node's tail

        self.tail = newNode

    def print_forward(self):
        current_node = self.head  # ~# Starting from the head

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail  # ~# Starting from the tail

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.prev


dll = DoublyLinkedList()
dll.add_node(5)
dll.add_node(7)
dll.add_node(1)
dll.print_forward()
print("-" * 10)
dll.print_backward()
