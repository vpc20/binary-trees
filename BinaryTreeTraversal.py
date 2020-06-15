from collections import deque

from binarytree import tree

from BinaryTrees import binary_tree
from HeightOfATree import tree_height


def preorder_array(root):
    """
    Visit the root before the values in left and right subtree.

    :param root: root of the binary tree
    :return: preorder list of node values
    """

    def preorder(node):
        arr.append(node.val)
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

    arr = []
    preorder(root)
    return arr


def preorder_array_iterative(node):
    """
    Visit the root before the values in left and right subtree.

    :param node: root of the binary tree
    :return: preorder list of node values
    """

    stack = [node]
    arr = []
    while stack:
        node = stack.pop()
        arr.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return arr


def inorder_array(root):
    """
    Visit the root of a subtree between visiting the values in its left subtree and visiting those in its right
    subtree.

    :param root: root of the binary tree
    :return: inorder list of node values
    """

    def inorder(node):
        if node.left:
            inorder(node.left)
        arr.append(node.val)
        if node.right:
            inorder(node.right)

    arr = []
    inorder(root)
    return arr


def inorder_array_iterative(node):
    """
    Visit the root of a subtree between visiting the values in its left subtree and visiting those in its right
    subtree.

    :param node: root of the binary tree
    :return: inorder list of node values
    """
    arr = []
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            arr.append(node.val)
            node = node.right
    return arr


def postorder_array(root):
    """
    Visit the root after the values in left and right subtree.

    :param root: root of the binary tree
    :return: postorder list of node values
    """

    def postorder(node):
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        arr.append(node.val)

    arr = []
    postorder(root)
    return arr


def postorder_array_iterative(node):
    """
    Visit the root after the values in left and right subtree.

    :param node: root of the binary tree
    :return: postorder list of node values
    """

    stack = [node]
    arr = []
    while stack:
        node = stack.pop()
        arr.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return arr[::-1]


def level_order_array(node):
    """
    Visit every node on a level before going to a lower level.

    :param node: root of the binary tree
    :return: level-order list of node values
    """
    arr = []
    q = deque([node])
    while q:
        node = q.popleft()
        arr.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return arr


def level_order_array_recursive(node):
    """
    Visit every node on a level before going to a lower level.

    :param node: root of the binary tree
    :return: level-order list of node values
    """

    def print_level(node, level):
        if node:  # preorder walk, but print only the last level
            if level == 0:
                arr.append(node.val)
                return
            print_level(node.left, level - 1)
            print_level(node.right, level - 1)

    arr = []
    for i in range(tree_height(node) + 1):
        print_level(node, i)
    return arr


if __name__ == '__main__':
    # t = tree()  # generate a random binary tree and return its root node
    # print(t)

    t = binary_tree([7, 4, 10, 13, 3, 5, 6, None, None, 9, 8])

    print('preorder')
    # print([e.val for e in t.preorder])
    print(preorder_array(t))
    print(preorder_array_iterative(t))

    print('inorder')
    # print([e.val for e in t.inorder])
    print(inorder_array(t))
    print(inorder_array_iterative(t))

    print('postorder')
    # print([e.val for e in t.postorder])
    print(postorder_array(t))
    print(postorder_array_iterative(t))

    print('levelorder')
    # print([e.val for e in t.levelorder])
    print(level_order_array(t))
    print(level_order_array_recursive(t))
