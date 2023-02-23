class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.tail = None


class SentinelList:
    def __init__(self):
        self.head = Node(None)  # * Assigning guardain node at head
        self.tail = Node(None)  # * Assigning guardian node at tail

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_back(self, value):
        current_node = Node(value)

        current_node.next = self.tail
        current_node.prev = self.tail.prev

        self.tail.prev.next = current_node
        self.tail.prev = current_node

    def add_node_front(self, value):
        current_node = Node(value)

        current_node.prev = self.head
        current_node.next = self.head.next

        self.head.next.prev = current_node
        self.head.next = current_node

    def print_forward(self):
        current_node = self.head.next
        while current_node is not self.tail:
            print(current_node.value)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail.prev
        while current_node is not self.head:
            print(current_node.value)
            current_node = current_node.prev

    def delete_node(self, value):
        current_node = self.head.next

        while current_node is not self.tail:
            if current_node.value is value:
                print("Found the node to delete ==>", current_node.value)
                # ~# Just change the pointers of prev and next nodes

                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

            current_node = current_node.next

    def insertAfter(self, searchValue, insertValue):
        current_node = self.head.next

        while current_node is not self.tail:
            if current_node.value is searchValue:
                spot = Node(insertValue)

                spot.prev = current_node
                spot.next = current_node.next

                current_node.next.prev = spot
                current_node.next = spot

                return True

            current_node = current_node.next


########################################################################

SLL = SentinelList()
SLL.add_node_back(5)
SLL.add_node_back(7)
SLL.insertAfter(5, 4)
SLL.add_node_back(1)
SLL.add_node_back(9)

print("-" * 10)
SLL.print_forward()
print("-" * 10)
SLL.print_backward()
print("-" * 10)
