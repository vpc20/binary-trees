from collections import deque
from BinaryTrees import TreeNode


def depth(root, node):
    """
    The depth of a node is the length of the simple path from the root the node.

    :param root: root of the tree
    :param node: node of the tree
    :return: depth of the node
    """

    def dfs(curr, lvl):
        nonlocal d
        if curr == node:
            d = lvl
            return True
        if curr.left:
            if dfs(curr.left, lvl + 1):
                return True
        if curr.right:
            if dfs(curr.right, lvl + 1):
                return True

    d = 0
    if root is None or node is None:
        return 0
    dfs(root, 0)
    return d


def depth_iterative(root, node):
    lvl = -1
    q = deque([root])
    while q:
        lvl += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == node:
                return lvl
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return 0


if __name__ == '__main__':
    node4 = TreeNode(4)
    print(node4)
    print(depth(node4, node4))
    print(depth_iterative(node4, node4))

    node2 = TreeNode(2)
    node4.left = node2
    print(node4)
    print(depth(node4, node2))
    print(depth_iterative(node4, node2))

    node6 = TreeNode(6)
    node4.right = node6
    print(node4)
    print(depth(node4, node6))
    print(depth_iterative(node4, node6))

    node1 = TreeNode(1)
    node2.left = node1
    print(node4)
    print(depth(node4, node1))
    print(depth_iterative(node4, node1))
