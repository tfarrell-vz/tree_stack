import time


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def rec_preorder(self):
        """
        Preorder traversal:
        visit root - yield data
        visit left subtree, traverse preorder (recursive call)
        visit right subtree, traverse preorder (recursive call)
        """
        print(self.data)
        if self.left:
            self.left.rec_preorder()

        if self.right:
            self.right.rec_preorder()

    def rec_inorder(self):
        """
        Left, Root, Right
        """
        if self.left:
            self.left.rec_inorder()

        print(self.data)

        if self.right:
            self.right.rec_inorder()

    def rec_postorder(self):
        """
        Left, Right, Root
        """
        if self.left:
            self.left.rec_postorder()

        if self.right:
            self.right.rec_postorder()

        print(self.data)


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def preorder_traversal(self):
        """
        Use a stack to store the branches that still need to be traversed
        after a pass. A pass is complete when None is reached.
        """
        right_stack = []
        cursor = self.root
        while cursor:
            if cursor.right:
                right_stack.append(cursor.right)
            print(cursor.data)
            cursor = cursor.left

            # If we hit a leaf while going down the left, pop a
            # node off the stack and make a pass from that point.
            if not cursor:
                if len(right_stack) > 0:
                    cursor = right_stack.pop()

    def inorder_traversal(self):
        node_stack = []
        cursor = self.root

        while cursor:
            node_stack.append(cursor)

            if not cursor.left:
                while len(node_stack) > 0:
                    top = node_stack.pop()
                    print(top.data)

                    if top.right:
                        cursor = top.right
                        break

                    elif not top.right and len(node_stack) == 0:
                        cursor = None

            else:
                cursor = cursor.left

    def post_order_traversal(self):
        left_stack = []
        right_stack = []
        cursor = self.root

        while cursor:
            left_stack.append(cursor)

            if not cursor.left:
                if not cursor.right:
                    if len(right_stack) > 0:
                        print(right_stack.pop())

                    elif len(left_stack) > 0:
                        top = left_stack.pop()

                        if top.right:
                            right_stack.append(top)
                            cursor = top.right

                    else:
                        cursor = None


# Connect the nodes into a tree data structure.
def make_tree_one():
    """Constructs our tree."""

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

    nodeA.left = nodeB
    nodeA.right = nodeC

    nodeB.left = nodeD
    nodeB.right = nodeE

    nodeC.left = nodeF
    nodeC.right = nodeG

    # Ensure that the tree is arranged properly.
    for node in node_list:
        print(node.data)
        if node.left:
            print("Left:" + node.left.data)
        if node.right:
            print("Right:" + node.right.data)
        if not node.left and not node.right:
            print("leaf")
        print()

    return BinaryTree(nodeA)


def main():
    # Set up a tree.
    victory_tree = make_tree_one()

    print("Preorder using stack")
    start_time = time.time()
    victory_tree.preorder_traversal()
    end_time = time.time()
    time_elapsed = end_time-start_time
    print("Time elapsed: %s \n" % time_elapsed)

    print("Recursive preorder")
    start_time=time.time()
    victory_tree.root.rec_preorder()
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("Time elapsed: %s \n" % time_elapsed)

    print("Inorder using stack")
    victory_tree.inorder_traversal()
    print()

    print("Recursive postorder")
    victory_tree.root.rec_postorder()
    print()

    print("Postorder using stack")
    victory_tree.root.rec_postorder()
    print()


if __name__ == '__main__':
    main()
