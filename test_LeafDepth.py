from random import randint
from unittest import TestCase
from MaximumLeafDepth import max_leaf_depth
from MinimumLeafDepth import min_leaf_depth

from binarytree import tree


class Test(TestCase):
    def test_max_leaf_depth(self):
        for _ in range(1000):
            h = randint(0, 9)
            t = tree(height=h)
            # print(t.height)
            print(t)
            self.assertEqual(t.max_leaf_depth, max_leaf_depth(t))

    def test_min_leaf_depth(self):
        for _ in range(1000):
            h = randint(0, 9)
            t = tree(height=h)
            # print(t.height)
            print(t)
            self.assertEqual(t.min_leaf_depth, min_leaf_depth(t))
