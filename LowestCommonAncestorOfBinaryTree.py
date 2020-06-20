# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

# Example 1:
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA
# definition.
#
# Note:
# All of the nodes ' values will be unique.
# p and q are different and both values will exist in the binary tree.
from BinaryTrees import binary_tree


# def lowestCommonAncestor(self, root, p, q):
#     # Stack for tree traversal
#     stack = [root]
#
#     # Dictionary for parent pointers
#     parent = {root: None}
#
#     # Iterate until we find both the nodes p and q
#     while p not in parent or q not in parent:
#         node = stack.pop()
#         # While traversing the tree, keep saving the parent pointers.
#         if node.left:
#             parent[node.left] = node
#             stack.append(node.left)
#         if node.right:
#             parent[node.right] = node
#             stack.append(node.right)
#
#     # Ancestors set() for node p.
#     ancestors = set()
#
#     # Process all ancestors for node p using parent pointers.
#     while p:
#         ancestors.add(p)
#         p = parent[p]
#
#     # The first ancestor of q which appears in
#     # p's ancestor set() is their lowest common ancestor.
#     while q not in ancestors:
#         q = parent[q]
#     return q


def lowest_common_ancestor(root, p, q):
    def dfs(curr):
        if curr.left is not None:
            preds[curr.left] = curr
            dfs(curr.left)
        if curr.right is not None:
            preds[curr.right] = curr
            dfs(curr.right)

    preds = {}
    dfs(root)

    pset = {p}
    while p != root:
        pset.add(preds[p])
        p = preds[p]

    if q in pset:
        return q
    while q != root:
        if preds[q] in pset:
            return preds[q]
        q = preds[q]


# def lowestCommonAncestor(root, p, q):
#     def recurse_tree(curr):
#         nonlocal ans
#         if not curr:
#             return False
#         left = recurse_tree(curr.left)
#         right = recurse_tree(curr.right)
#
#         mid = curr == p or curr == q
#         if mid + left + right >= 2:
#             ans = curr
#         return mid or left or right
#
#     ans = None
#     recurse_tree(root)
#     return ans


t = binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(t)
print(repr(lowest_common_ancestor(t, t.left, t.right)))

