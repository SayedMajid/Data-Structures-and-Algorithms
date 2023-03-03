class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size=10):
        self.table = [None] * size

    def hash(self, key):
        return key % len(self.table)

    def put(self, key, value):
        offset = self.hash(key)
        current = self.table[offset]
        while current is not None:
            if current.key == value:
                current.value = value
                return False

            current = current.next

        entry = Node(key, value)
        entry.next = self.table[offset]
        self.table[offset] = entry
        return True

    def get(self, key):
        current = self.table[self.hash(key)]

        while current is not None:
            if current.key is not None:
                return current.value
            current = current.next

        return False

    def print_hash_table(self):
        for offset in range(0, len(self.table)):
            print(f"{offset}: ", end=" ")
            current = self.table[offset]
            while current is not None:
                print(f"{{{current.key}, {current.value}}}", end=" ")
                current = current.next
            print()

    def remove(self, key):
        offset = self.hash(key)
        previous = self.table[offset]

        current = self.table[offset]
        while current is not None:
            if current.key == key:
                if current is self.table[offset]:
                    self.table[offset] = self.table[offset].next
                else:
                    previous.next = current.next
                return True

            previous, current = current, current.next

        return False


HT = HashTable()
HT.put(224, "BigB")
HT.put(420, "SmallB")
HT.put(420, "SmallA")
HT.put(420, "SmallC")
HT.print_hash_table()
print(HT.get(224))
# HT.remove()
