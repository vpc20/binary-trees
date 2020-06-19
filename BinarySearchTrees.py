from BinaryTrees import print_binary_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        print_binary_tree(self)
        return ''

    def __repr__(self):
        return 'Node(' + str(self.val) + ')'


def binary_search_tree(n):
    def bst(arr):
        mid = len(arr) // 2
        node = TreeNode(arr[mid])
        if len(arr[:mid]) > 0:
            node.left = bst(arr[:mid])
        if len(arr[mid + 1:]) > 0:
            node.right = bst(arr[mid + 1:])
        return node

    if not n:
        return None
    arr = list(range(1, n + 1))
    return bst(arr)


def tree_insert(node, val):
    parent = None
    while node:
        parent = node
        if val < node.val:
            node = node.left
        else:
            node = node.right

    new_node = TreeNode(val, parent=parent)
    if parent is not None:
        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node


def tree_search(node, val):
    while node and val != node.val:
        if val < node.val:
            node = node.left
        else:
            node = node.right
    return node


def tree_minimum(node):
    while node.left:
        node = node.left
    return node


def tree_maximum(node):
    while node.right:
        node = node.right
    return node


bst = binary_search_tree(15)
print(bst)
print(tree_minimum(bst))
print(tree_maximum(bst))
print(tree_search(bst, 7))
