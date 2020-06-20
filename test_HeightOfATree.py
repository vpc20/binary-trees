from unittest import TestCase
from binarytree import tree
from random import randint
from HeightOfATree import tree_height, tree_height_iterative


class Test(TestCase):
    def test_height(self):
        for _ in range(1000):
            h = randint(0, 9)
            t = tree(height=h)
            # print(t.height)
            # print(t)
            self.assertEqual(t.height, tree_height(t))
            self.assertEqual(t.height, tree_height_iterative(t))
