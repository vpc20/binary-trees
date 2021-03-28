from collections import deque
from BinaryTrees import binary_tree


def min_leaf_depth(root):
    if root is None:
        return 0
    lvl = -1
    q = deque([root])
    while q:
        lvl += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr.left is None and curr.right is None:
                return lvl
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return 0


if __name__ == '__main__':
    t = binary_tree([3, 9, 20, None, None, 15, 7])
    print(t)
    print(min_leaf_depth(t))

    t = binary_tree([2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5])
    print(t)
    print(min_leaf_depth(t))

    t = binary_tree([2, 0, 1])
    print(t)
    print(min_leaf_depth(t))
