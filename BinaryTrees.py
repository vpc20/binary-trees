from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node(' + str(self.val) + ')'


def binary_tree(vals):
    """
     Create binary tree from level-order list of node values

     :param vals: list representation of binary tree
     :return: root of the tree
     """
    nodes = [TreeNode(v) if v else None for v in vals]
    root = nodes[0]
    for i, node in enumerate(nodes):
        if vals[i] is not None:
            l = i * 2 + 1
            if l < len(vals):
                node.left = nodes[l]
            r = i * 2 + 2
            if r < len(vals):
                node.right = nodes[r]
    return root


def print_preorder(root):
    def preorder(node):
        print(node.val, end=' ')
        if node.left is not None:
            preorder(node.left)
        if node.right is not None:
            preorder(node.right)

    preorder(root)
    print('')


def print_inorder(root):
    def inorder(node):
        if node.left is not None:
            inorder(node.left)
        print(node.val, end=' ')
        if node.right is not None:
            inorder(node.right)

    inorder(root)
    print('')


def print_postorder(root):
    def postorder(node):
        if node.left is not None:
            postorder(node.left)
        if node.right is not None:
            postorder(node.right)
        print(node.val, end=' ')

    postorder(root)
    print('')


def print_level_order(node):
    q = deque([node])
    while q:
        node = q.popleft()
        print(node.val, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print('')


def print_graphviz(node):
    print('digraph BST {')
    print('  node [shape=circle];')

    i = 0
    q = deque([node])
    while q:
        node = q.popleft()
        if node.left or node.right:
            if node.left:
                print(f'  {node.val} -> {node.left.val};')
            else:
                i += 1
                print(f'  n{i} [style=invis];')
                print(f'  {node.val} -> n{i} [style=invis];')

            i += 1
            print(f'  n{i} [style=invis];')
            print(f'  {node.val} -> n{i} [style=invis];')

            if node.right:
                print(f'  {node.val} -> {node.right.val};')
            else:
                i += 1
                print(f'  n{i} [style=invis];')
                print(f'  {node.val} -> n{i} [style=invis];')

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    print('}')
