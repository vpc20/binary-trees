# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent
# nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
from collections import defaultdict

from BinaryTrees import binary_tree


def path_sum(root, sum):
    def dfs(node, prevsum, sum):
        if not node:
            return

        nonlocal count
        currsum = prevsum + node.val
        if currsum - sum in sums:
            count += sums[currsum - sum]

        sums[currsum] += 1
        dfs(node.left, currsum, sum)
        dfs(node.right, currsum, sum)
        sums[currsum] -= 1

    count = 0
    sums = defaultdict(int, {0: 1})
    dfs(root, 0, sum)
    return count


# def path_sum(root, sum):
#     def dfs(node, prefs, prefsum):
#         nonlocal count
#         prefsum += node.val
#         x = prefsum - sum
#         if x in prefs:
#             count += prefs[x]
#         if node.left or node.right:
#             prefs[prefsum] = prefs[prefsum] + 1 if prefsum in prefs else 1
#         if node.left:
#             dfs(node.left, prefs, prefsum)
#         if node.right:
#             dfs(node.right, prefs, prefsum)
#
#     if root is None:
#         return 0
#     if root.left is None and root.right is None:
#         return 1 if root.val == sum else 0
#     count = 0
#     dfs(root, {}, 0)
#     return count


t = binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
print(t)
print(path_sum(t, 8))
