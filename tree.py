class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.level = 1

    # ~* Recursive function
    def addNode(self, node, value):
        # ~# Ending Condition

        # ~* Node is created here!!!
        if node is None:
            return Node(value)

        # ~# This ie where the node addition takes place
        if value > node.value:
            node.right = self.addNode(node.right, value)
        else:
            node.left = self.addNode(node.left, value)

        return node

    def printTree(self, node):
        if node != None:
            self.level += 1
            self.printTree(node.left)
            print("     " * self.level, node.value)
            self.printTree(node.right)
            self.level -= 1

    def printDesc(self, node):
        if node:
            self.printDesc(node.right)
            print(node.value)
            self.printDesc(node.left)

    def removeNode(self, node, value):
        # ~% 1. The value was not found
        if node == None:
            return None

        # ~% 2. Find the node either left or right
        if value > node.value:
            node.right = self.removeNode(node.right, value)
        elif value < node.value:
            node.left = self.removeNode(node.left, value)
        else:
            # ~! Node found...
            #! 1. There are no children - Uda do saale ko
            if node.left == None and node.right == None:
                print("Node removed =====>", node.value)
                return None

            #! 2. There is left child but no right child
            if node.left != None and node.right == None:
                return node.left

            #! 3. There is right child but no left child
            if node.left == None and node.right != None:
                return node.right

            #! 4. Both children are present
            successor = successor.right

            while successor.left != None:
                successor = successor.left

            node.value = successor.value
            node.right = self.removeNode(node.right, successor.value)

        return node


BST = Tree()
BST.root = BST.addNode(BST.root, 5)
BST.root = BST.addNode(BST.root, 7)
BST.root = BST.addNode(BST.root, 1)
BST.root = BST.addNode(BST.root, 2)
BST.root = BST.addNode(BST.root, 6)
BST.root = BST.addNode(BST.root, 9)
BST.root = BST.addNode(BST.root, 3)


BST.printTree(BST.root)
print("-" * 10)
BST.removeNode(BST.root, 1)
print("-" * 10)
BST.printTree(BST.root)
