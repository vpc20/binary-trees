# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
from BinaryTrees import binary_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    def dfs(curr, lvl):
        if lvl < len(result):
            result[lvl].append(curr.val)
        else:
            result.append([curr.val])
        if curr.left is not None:
            dfs(curr.left, lvl + 1)
        if curr.right is not None:
            dfs(curr.right, lvl + 1)

    if root is None:
        return []
    result = []
    dfs(root, 0)
    return result


# def level_order(self, root: TreeNode) -> List[List[int]]:
#     if not root:
#         return []
#     queue = deque([root])
#     result = []
#
#     while queue:
#         result.append([])
#         count = len(queue)
#         for _ in range(count):
#             node = queue.popleft()
#             result[-1].append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#     return result


arr = [3, 9, 20, None, None, 15, 7]
t = binary_tree(arr)
print(level_order(t))
