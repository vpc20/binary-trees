# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where
# each path's sum equals targetSum.
#
# A leaf is a node with no children.
#
# Example 1:
# Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
# Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
#
# Example 2:
# Input: root = [1, 2, 3], targetSum = 5
# Output: []
#
# Example 3:
# Input: root = [1, 2], targetSum = 0
# Output: []
#
# Constraints:
#
# The number of nodes in the tree is in the range[0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
from BinaryTrees import binary_tree


def path_sum(root, sum):
    def dfs(node, accsum, path):
        if node.left is None and node.right is None:
            if accsum == sum:
                result.append(path)
            return
        if node.left is not None:
            dfs(node.left, accsum + node.left.val, path + [node.left.val])
        if node.right is not None:
            dfs(node.right, accsum + node.right.val, path + [node.right.val])

    if root is None:
        return []

    result = []
    dfs(root, root.val, [root.val])
    return result


t1 = binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
print(t1)
print(path_sum(t1, 22))
