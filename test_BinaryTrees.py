from unittest import TestCase

from binarytree import tree

from BinaryTrees import *


class Test(TestCase):
    def test_binary_tree(self):
        for _ in range(10000):
            t = tree()  # Generate a random binary tree and return its root node
            # print(t)
            bt = binary_tree(t.values)
            self.assertEqual([e.val for e in t.preorder], preorder_array(bt))
            self.assertEqual([e.val for e in t.preorder], preorder_array_iterative(bt))
            self.assertEqual([e.val for e in t.inorder], inorder_array(bt))
            self.assertEqual([e.val for e in t.inorder], inorder_array_iterative(bt))
            self.assertEqual([e.val for e in t.postorder], postorder_array(bt))
            self.assertEqual([e.val for e in t.postorder], postorder_array_iterative(bt))
            self.assertEqual([e.val for e in t.levelorder], level_order_array(bt))
            self.assertEqual([e.val for e in t.levelorder], level_order_array_recursive(bt))

    def test_binary_tree_values(self):
        for _ in range(10000):
            t = tree()
            # print(t)
            bt = binary_tree(t.values)
            # print(bt)

            self.assertEqual(t.values, binary_tree_values(bt))

    # def test_random_binary_tree(self):
    #     bt = random_binary_tree()
    #     print_binary_tree(bt)
