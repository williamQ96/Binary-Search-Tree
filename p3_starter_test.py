#
#   NOTE: THIS IS NOT AN EXHAUSTIVE TEST FILE.
#   YOU MUST DEVELOP MORE TEST CASES THAN WHAT ARE PROVIDED.
#

from submissions.vietl import *
import pytest

def buildBalancedTree():
    """
    Description: This function builds and returns a tree of the following format:
                                        30
                               20              40
                           15      25      35      45
                         13  17  23  27  33  37  43  47
                                   24
    Returns: (<BinarySearchTree>, [<BSTNode>, ...])
    """
    BST = BinarySearchTree()

    v = "a"
    N0 = BSTNode((30, v)) # root of the tree

    N1 = BSTNode((20, v)) #first level
    N2 = BSTNode((40, v))

    N3 = BSTNode((15, v)) #second level
    N4 = BSTNode((25, v))
    N5 = BSTNode((35, v))
    N6 = BSTNode((45, v))

    N7 = BSTNode((13, v)) #Third level
    N8 = BSTNode((17, v))
    N9 = BSTNode((23, v))
    N10 = BSTNode((27, v))
    N11 = BSTNode((33, v))
    N12 = BSTNode((37, v))
    N13 = BSTNode((43, v))
    N14 = BSTNode((47, v))

    N0.setLChild(N1)
    N0.setRChild(N2)
    N1.setParent(N0)
    N2.setParent(N0)

    N1.setLChild(N3)
    N1.setRChild(N4)
    N3.setParent(N1)
    N4.setParent(N1)

    N2.setLChild(N5)
    N2.setRChild(N6)
    N5.setParent(N2)
    N6.setParent(N2)

    N3.setLChild(N7)
    N3.setRChild(N8)
    N7.setParent(N3)
    N8.setParent(N3)

    N4.setLChild(N9)
    N4.setRChild(N10)
    N9.setParent(N4)
    N10.setParent(N4)

    N5.setLChild(N11)
    N5.setRChild(N12)
    N11.setParent(N5)
    N12.setParent(N5)

    N6.setLChild(N13)
    N6.setRChild(N14)
    N13.setParent(N6)
    N14.setParent(N6)

    BST._root = N0
    return (BST, [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14])


class TestMain:

    def test_initValid(self):
        BST = BinarySearchTree()
        assert BST._root == None

    def test_insertValidEmpty(self):
        tree = BinarySearchTree()
        T1 = (30, "a")

        ret = tree.insert(T1)

        assert ret == True
        assert tree._root.getValue() is T1
        root = tree._root
        assert root.getParent() == root.getRChild() == root.getLChild() == None

    def test_insertValid(self):
        BST, nodes = buildBalancedTree()
        print(BST.traverse("pre-order"))
        val = "a"
        T1 = (-10, val)
        T2 = (50, val)
        T3 = (31, val)

        ret1 = BST.insert(T1)
        ret2 = BST.insert(T2)
        ret3 = BST.insert(T3)

        assert ret1 == ret2 == ret3 == True, "insert failed to return True on valid call\n"
        p1, p2, p3 = nodes[7], nodes[14], nodes[11]
        c1, c2, c3 = p1.getLChild(), p2.getRChild(), p3.getLChild()

        assert c1.getValue() is T1, f"Node: {T1[0]} is not in the right place. Should be left child of parent {p1._key}\n"
        assert c2.getValue() is T2, f"Node: {T2[0]} is not in the right place. Should be right child of parent {p2._key}\n"
        assert c3.getValue() is T3, f"Node: {T3[0]} is not in the right place. Should be left child of parent {p3._key}\n"

        assert c1.getParent() is p1, f"Node: {c1._key} should have parent {p1._key}. It has parent {c1.getParent()._key}\n"
        assert c2.getParent() is p2, f"Node: {c2._key} should have parent {p2._key}. It has parent {c2.getParent()._key}\\n"
        assert c3.getParent() is p3, f"Node: {c3._key} should have parent {p3._key}. It has parent {c3.getParent()._key}\\n"

    def test_insertInvalid(self):
        BST = BinarySearchTree()

        T1 = ("a", 1)
        T2 = []
        T3 = None
        T4 = (1)

        ret1 = BST.insert(T1)
        ret2 = BST.insert(T2)
        ret3 = BST.insert(T3)
        ret4 = BST.insert(T4)

        assert ret1 == ret2 == ret3 == ret4 == False
        assert BST._root == None

    def test_deleteValidRoot(self):
        BST, nodes = buildBalancedTree()
        id1 = 30
        root = BST._root
        successor = nodes[11]
        succParent = successor.getParent()
        inorder = "13, 15, 17, 20, 23, 25, 27, 33, 35, 37, 40, 43, 45, 47"

        ret = BST.delete(id1)

        assert ret == True
        assert succParent.getLChild() == None
        assert "30" not in BST.traverse("pre-order")
        assert BST.traverse("in-order") == inorder
        assert BST._root._key == successor._key
        assert BST._root.getLChild()._key == 20
        assert BST._root.getRChild()._key == 40

    def test_deleteValidLeaf(self):
        BST, nodes = buildBalancedTree()
        id1 = 13
        parent = nodes[3]
        node = nodes[7]
        inorder = "15, 17, 20, 23, 25, 27, 30, 33, 35, 37, 40, 43, 45, 47"

        ret = BST.delete(id1)

        assert ret == True
        assert node.getParent() == node.getLChild() == node.getRChild() == None
        assert "13" not in BST.traverse("pre-order")
        assert BST.traverse("in-order") == inorder
        assert parent._key == 15
        assert parent.getRChild()._key == 17
        assert parent.getParent()._key == 20

    def test_deleteValidOneChild(self):
        BST, nodes = buildBalancedTree()
        id1 = 15
        parent = nodes[1]
        node = nodes[3]
        temp = nodes[7]
        temp.setParent(None)
        node.setLChild(None)
        inorder = "17, 20, 23, 25, 27, 30, 33, 35, 37, 40, 43, 45, 47"

        ret = BST.delete(id1)

        assert ret == True
        assert parent.getLChild()._key == 17
        assert node.getParent() == node.getLChild() == node.getRChild() == None
        assert "15" not in BST.traverse("pre-order")
        assert BST.traverse("in-order") == inorder
        assert parent._key == 20
        assert parent.getLChild()._key == 17
        assert parent.getRChild()._key == 25
        assert parent.getParent()._key == 30

    def test_deleteValidNotInTree(self):
        BST, nodes = buildBalancedTree()
        id1 = 31
        inorder = "13, 15, 17, 20, 23, 25, 27, 30, 33, 35, 37, 40, 43, 45, 47"

        ret = BST.delete(id1)

        assert ret == False
        assert BST.traverse("in-order") == inorder

    def test_deleteInvalid(self):
        BST = BinarySearchTree()
        id = 10

        with pytest.raises(TreeIsEmpty):
            ret = BST.delete(id)

        assert BST._root == None

    def test_findValidInTree(self):
        BST, nodes = buildBalancedTree()
        id1 = 15
        inorder = "13, 15, 17, 20, 23, 25, 27, 30, 33, 35, 37, 40, 43, 45, 47"

        ret = BST.find(id1)

        assert type(ret) == tuple
        assert len(ret) == 2
        assert ret[0] == 15
        assert BST.traverse("in-order") == inorder

    def test_findValidNotInTree(self):
        BST, nodes = buildBalancedTree()
        id1 = 31
        inorder = "13, 15, 17, 20, 23, 25, 27, 30, 33, 35, 37, 40, 43, 45, 47"

        ret = BST.find(id1)

        assert ret == False
        assert BST.traverse("in-order") == inorder

    def test_findInvalidEmpty(self):
        BST = BinarySearchTree()
        id1 = 15

        with pytest.raises(TreeIsEmpty):
            ret = BST.find(id1)

    def test_findInvalidFormat(self):
        BST, nodes = buildBalancedTree()
        id1 = "13"
        id2 = None
        id3 = []
        id4 = (13, "a")
        id5 = 13.4
        inorder = "13, 15, 17, 20, 23, 25, 27, 30, 33, 35, 37, 40, 43, 45, 47"
        ret1 = ret2 = ret3 = ret4 = ret5 = False
        try:
            ret1 = BST.find(id1)
        except:
            pass
        try:
            ret2 = BST.find(id2)
        except:
            pass
        try:
            ret3 = BST.find(id3)
        except:
            pass
        try:
            ret4 = BST.find(id4)
        except:
            pass
        try:
            ret5 = BST.find(id5)
        except:
            pass

        assert ret1 == ret2 == ret3 == ret4 == ret5 == False
        assert BST.traverse("in-order") == inorder
