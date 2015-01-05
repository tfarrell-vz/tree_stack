class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def preorder_traversal(self):
        """
        Use a stack to store the branches that still need to be traversed
        after a pass. A pass is complete when None is reached.
        """
        self.right_stack = []
        cursor = self.root
        while cursor:
            if cursor.right:
                self.right_stack.append(cursor.right)
            print(cursor.data)
            cursor = cursor.left

            # If we hit a leaf while going down the left, pop a
            # node off the stack and make a pass from that point.
            if not cursor:
                if len(self.right_stack) > 0:
                    cursor = self.right_stack.pop()

# Make some nodes for the tree.
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")

# Put the nodes in a list.
node_list = []
node_list.extend((nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG))

# Connect the nodes into a tree data structure.
nodeA.left = nodeB
nodeA.right = nodeC

nodeB.left = nodeD
nodeB.right = nodeE

nodeC.left = nodeF
nodeC.right = nodeG

# Ensure that the tree is arranged properly
for node in node_list:
    print(node.data)
    if node.left:
        print("Left:" + node.left.data)
    if node.right:
        print("Right:" + node.right.data)
    if not node.left and not node.right:
        print("leaf")
    print()

# Set up a tree and traverse it
victory_tree = BinaryTree(nodeA)
victory_tree.preorder_traversal()


