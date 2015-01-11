from tree import Node, BinaryTree

nodeA, nodeB, nodeC, nodeD = Node("A"), Node("B"), Node("C"), Node("D")
nodeE, nodeF, nodeG = Node("E"), Node("F"), Node("G")

nodeA.left = nodeB
nodeA.right = nodeC

nodeB.left = nodeD
nodeB.right = nodeE

nodeC.left = nodeF
nodeC.right = nodeG

tree_one = BinaryTree(nodeA)

class TestNode:
    def test_recursive_preorder(self, capsys):
        nodeA.rec_preorder()
        out, err = capsys.readouterr()
        assert out == "\n".join(["A", "B", "D", "E", "C", "F", "G\n"])

    def test_recursive_inorder(self, capsys):
        nodeA.rec_inorder()
        out, err = capsys.readouterr()
        assert out == "\n".join(["D", "B", "E", "A", "F", "C", "G\n"])

    def test_recursive_postorder(self, capsys):
        nodeA.rec_postorder()
        out, err = capsys.readouterr()
        assert out == "\n".join(["D", "E", "B", "F", "G", "C", "A\n"])
