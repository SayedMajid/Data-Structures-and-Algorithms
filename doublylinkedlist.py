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

    def delete_node(self, value):
        current_node = self.head

        # ~# Search for the value
        # * Start from head, if not found go to current.next and stop when its None(null)

        while current_node is not None:
            if current_node.value is value:
                # ~! Laavaris node xD
                if current_node is self.head and current_node is self.tail:
                    print("Removing the only node", current_node.value)
                    self.head = None
                    self.tail = None
                    return True

                # ~! Checking if its the first node
                if current_node is self.head:
                    print("Removing the first node", current_node.value)
                    self.head = self.head.next
                    self.head.prev = None
                    return True

                # ~! Checking if its the last node
                if current_node is self.tail:
                    print("Removing the tail node", current_node.value)
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return True

                # ~! Deleting node anywhere from the middle of DLL
                print("Removing", current_node.value)
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

            current_node = current_node.next


dll = DoublyLinkedList()
dll.add_node(5)
dll.add_node(7)
dll.add_node(9)
dll.add_node(1)
dll.print_forward()
print("-" * 10)
dll.print_backward()

dll.delete_node(1)
dll.delete_node(5)
dll.delete_node(9)
dll.delete_node(7)
dll.print_forward()
