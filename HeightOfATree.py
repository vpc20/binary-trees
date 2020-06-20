from collections import deque

from binarytree import tree


def tree_height(node):
    """
    The height of a node in a tree is the number of edges on the longest simple downward path from the node to a leaf,
    and the height of a tree is the height of its root. The height of a tree is also equal to the largest depth of
    any node in the tree.

    :param node: node of the tree
    :return: height of the node
    """

    left = right = 0
    if node.left:
        left = 1 + tree_height(node.left)
    if node.right:
        right = 1 + tree_height(node.right)
    return max(left, right)


def tree_height_iterative(node):
    lvl = -1
    q = deque([node])
    while q:
        lvl += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return lvl


if __name__ == '__main__':
    # t = tree(height=3, is_perfect=False)
    t = tree()
    print(t)
    print(tree_height(t))
    print(tree_height_iterative(t))
