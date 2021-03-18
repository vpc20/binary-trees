from random import randint
from unittest import TestCase
from BinaryTrees import random_binary_tree
from DepthOfANode import depth, depth_iterative


class Test(TestCase):
    def preorder(self, root, node):
        print(depth(root, node))
        if node:
            self.assertEqual(depth(root, node), depth_iterative(root, node))
            if node.left:
                self.preorder(root, node.left)
            if node.right:
                self.preorder(root, node.right)

    def test_depth(self):
        for _ in range(1000):
            t = random_binary_tree()
            print(t)
            self.preorder(t, t)
