from unittest import TestCase
from binarytree import tree
from random import randint

from CompleteBinaryTree import tree_is_complete


class Test(TestCase):
    def test_tree_is_complete(self):
        for _ in range(1000):
            h = randint(0, 9)
            t = tree(height=h)
            print(t.is_complete)
            print(t)
            self.assertEqual(t.is_complete, tree_is_complete(t))

