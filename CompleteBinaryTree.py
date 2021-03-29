from collections import deque

from BinaryTrees import binary_tree


def tree_is_complete(root):
    if not root:
        return True
    q = deque([root])

    while q:
        lvlarr = []
        for _ in range(len(q)):
            node = q.popleft()
            if len(lvlarr) > 0:
                if node and node.val is not None and lvlarr[-1] is None:
                    return False
            lvlarr.append(node.val if node is not None else None)
            q.append(node.left if node is not None else None)
            q.append(node.right if node is not None else None)
        # print(lvlarr)
        if set(q) == {None}:  # q contains all Nones
            break
        if lvlarr[-1] is None:
            return False
    return True


# t = binary_tree([1])
# t = binary_tree([])
# t = binary_tree([1, 2, 3, 4, 5, 6, 7])
# print(t)
# print(level_order(t))

for i in range(1, 9):
    t = binary_tree([n for n in range(1, i)])
    # print(t)
    # print(tree_is_complete(t))
    assert tree_is_complete(t) is True

t = binary_tree([1, None, 2])
assert tree_is_complete(t) is False
t = binary_tree([1, 2, 3, None, 5])
assert tree_is_complete(t) is False
t = binary_tree([1, 2, 3, 4, None, 6])
assert tree_is_complete(t) is False
t = binary_tree([1, 2, 3, 4, 5, None, 7])
assert tree_is_complete(t) is False
t = binary_tree([1, 2, None, 4, 5])
assert tree_is_complete(t) is False
