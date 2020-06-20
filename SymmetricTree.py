# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Follow up: Solve it both recursively and iteratively.
from collections import deque

from BinaryTrees import binary_tree


def is_symmetric(root):
    def is_sym(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and is_sym(root1.left, root2.right) and is_sym(root1.right, root2.left)

    return is_sym(root, root)


# def is_symmetric(root):
#     def is_sym(root1, root2):
#         if root1 is None and root2 is None:
#             return True
#         if root1 is None or root2 is None:
#             return False
#         if root1.val != root2.val:
#             return False
#         if not is_sym(root1.left, root2.right):
#             return False
#         if not is_sym(root1.right, root2.left):
#             return False
#         return True
#
#     return is_sym(root, root)


def is_symmetric_iter(root):
    q = deque([root, root])

    while q:
        t1 = q.popleft()
        t2 = q.popleft()
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        q.append(t1.left)
        q.append(t2.right)
        q.append(t1.right)
        q.append(t2.left)

    return True


t = binary_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5])
print(t)
print(is_symmetric(t))
print(is_symmetric_iter(t))
