import sys
from collections import deque

from BinaryTrees import binary_tree


def is_valid_bst(root):
    def inorder(curr):
        nonlocal prevval
        if curr.left:
            if inorder(curr.left) is False:
                return False

        if prevval is not None and curr.val <= prevval:
            return False
        else:
            prevval = curr.val

        if curr.right:
            if inorder(curr.right) is False:
                return False
        return True

    if root is None:
        return True
    prevval = None
    return inorder(root)


def is_valid_bst_iter(root):
    if root is None:
        return True
    q = deque([(root, -sys.maxsize, sys.maxsize)])
    while q:
        curr, lo, hi = q.popleft()
        val = curr.val
        if lo >= val or hi <= val:
            return False
        if curr.left:
            q.append((curr.left, lo, val))
        if curr.right:
            q.append((curr.right, val, hi))
    return True


def is_valid_bstx(curr):
    prevval = -sys.maxsize
    stack = []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            if prevval >= curr.val:
                return False
            else:
                prevval = curr.val
            curr = curr.right
    return True


t = binary_tree([10, 5, 15, None, None, 6, 20])
print(t)
print(is_valid_bst(t))
print(is_valid_bst_iter(t))
