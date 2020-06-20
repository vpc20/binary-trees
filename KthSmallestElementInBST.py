# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
from BinaryTrees import binary_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def kth_smallest(root, k):
#     def inorder(curr):
#         nonlocal inord, retval
#         if curr.left:
#             if inorder(curr.left):
#                 return True
#         if k == inord:
#             retval = curr.val
#             return True
#         inord += 1
#         if curr.right:
#             if inorder(curr.right):
#                 return True
#
#     inord = 1
#     retval = None
#     inorder(root)
#     return retval

def kth_smallest(curr, k):
    stack = []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


t = binary_tree([5, 3, 6, 2, 4, None, None, 1])
print(t)
print(kth_smallest(t, 3))
