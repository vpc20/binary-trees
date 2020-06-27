from unittest import TestCase

from binarytree import tree, build

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
        for _ in range(20000):
            t = tree()
            # print(t)
            bt = binary_tree(t.values)
            # print(bt)

            self.assertEqual(t.values, binary_tree_values(bt))

    def test_random_binary_tree(self):
        for _ in range(10000):
            bt = random_binary_tree()
            if bt is not None:
                print_binary_tree(bt)
                vals = binary_tree_values(bt)
                print(vals)
                t = build(vals)
                self.assertEqual([e.val for e in t.preorder], preorder_array(bt))
                self.assertEqual([e.val for e in t.preorder], preorder_array_iterative(bt))
                self.assertEqual([e.val for e in t.inorder], inorder_array(bt))
                self.assertEqual([e.val for e in t.inorder], inorder_array_iterative(bt))
                self.assertEqual([e.val for e in t.postorder], postorder_array(bt))
                self.assertEqual([e.val for e in t.postorder], postorder_array_iterative(bt))
                self.assertEqual([e.val for e in t.levelorder], level_order_array(bt))
                self.assertEqual([e.val for e in t.levelorder], level_order_array_recursive(bt))

