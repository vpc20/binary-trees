# Given a binary tree, we install cameras on the nodes of the tree.
#
# Each camera at a node can monitor its parent, itself, and its immediate children.
#
# Calculate the minimum number of cameras needed to monitor all nodes of the tree.
#
# Example 1:
# Input: [0, 0, null, 0, 0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
# Example 2:
# Input: [0, 0, null, 0, null, 0, null, null, 0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree.The above image shows one
# of the valid configurations of camera placement.
#
# Note:
# The number of nodes in the given tree will be in the range[1, 1000].
# Every node has value 0.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import permutations

from BinaryTrees import binary_tree


def min_camera_cover(root):  # time limit exceeded
    def dfs(node, pred):
        nset.add(node)
        parent[node] = pred
        if node.left is not None:
            dfs(node.left, node)
        if node.right is not None:
            dfs(node.right, node)

    mincount = 1000
    parent = {}
    nset = set()
    dfs(root, None)
    # print(nset)
    # print(parent)
    for perm in permutations(nset):
        tempset = set()
        count = 0
        for node in perm:
            if parent[node] is not None:
                tempset.add(parent[node])
            if node.left is not None:
                tempset.add(node.left)
            if node.right is not None:
                tempset.add(node.right)
            tempset.add(node)
            count += 1
            if len(nset) == len(tempset):
                break
        mincount = min(mincount, count)
    return mincount


# def min_camera_cover(root):  # incorrect
#     def dfs(node, pred):
#         adjcount = 0
#         nset.add(node)
#
#         if pred is not None:
#             adjcount += 1
#         parent[node] = pred
#         if node.left is not None:
#             dfs(node.left, node)
#             adjcount += 1
#         if node.right is not None:
#             dfs(node.right, node)
#             adjcount += 1
#
#         degrees.append([node, adjcount])
#
#     mincount = 0
#     degrees = []
#     parent = {}
#     nset = set()
#     dfs(root, None)
#     nset1 = nset.copy()
#     print(nset)
#     print(parent)
#     tempset = set()
#     degrees.sort(key=lambda x: x[1], reverse=True)
#     print(degrees)
#     for node, _ in degrees:
#         if node not in nset1:
#             continue
#         if parent[node] is not None:
#             tempset.add(parent[node])
#         if node.left is not None:
#             tempset.add(node.left)
#         if node.right is not None:
#             tempset.add(node.right)
#         tempset.add(node)
#         nset1.remove(node)
#         mincount += 1
#         if len(nset) == len(tempset):
#             break
#     return mincount

# def min_camera_cover(root):  # incorrect
#     def dfs(node, pred):
#         adjcount = 0
#         nset.add(node)
#
#         if pred is not None:
#             adjcount += 1
#         parent[node] = pred
#         if node.left is not None:
#             dfs(node.left, node)
#             adjcount += 1
#         if node.right is not None:
#             dfs(node.right, node)
#             adjcount += 1
#
#         degrees.append([node, adjcount])
#
#     mincount = 0
#     degrees = []
#     parent = {}
#     nset = set()
#     dfs(root, None)
#     # print(nset)
#     # print(parent)
#     degrees.sort(key=lambda x: x[1], reverse=True)
#     # print(degrees)
#     for node, _ in degrees:
#         if node not in nset:
#             continue
#         if parent[node] in nset and parent[node] is not None:
#             nset.remove(parent[node])
#         if node.left in nset and node.left is not None:
#             nset.remove(node.left)
#         if node.right in nset and node.right is not None:
#             nset.remove(node.right)
#         if node in nset:
#             nset.remove(node)
#         mincount += 1
#         if len(nset) == 0:
#             break
#     return mincount


# t1 = binary_tree([1, 2, None, 3, 4])
# print(t1)
# print(min_camera_cover(t1))
#
# t2 = binary_tree([1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, None, 5])
# print(t2)
# print(min_camera_cover(t2))

# t3 = binary_tree([1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, None, 5])
# print(t3)
# print(min_camera_cover(t3))

t = binary_tree(
    [1,
     None, 2,
     None, None, None, 3,
     None, None, None, None, None, None, None, 4,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, 6, 7,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, 8, 9,
     ])
print(t)
print(min_camera_cover(t))
