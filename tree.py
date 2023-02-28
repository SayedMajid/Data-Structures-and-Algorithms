class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # ~* Recursive function
    def addNode(self, node, value):
        # ~# Ending Condition

        if node is None:
            return Node(value)

        # ~# value > node

        if value > node.value:
            node.right = self.addNode(node.right, value)
        else:
            node.left = self.addNode(node.left, value)

        return node

    def printTree(self, node):
        if node != None:
            self.printTree(node.left)
            print(node.value)
            self.printTree(node.right)

    def printDesc(self, node):
        if node:
            self.printDesc(node.right)
            print(node.value)
            self.printDesc(node.left)


BST = Tree()
BST.root = BST.addNode(BST.root, 5)
BST.root = BST.addNode(BST.root, 7)
BST.root = BST.addNode(BST.root, 1)

BST.printDesc(BST.root)
