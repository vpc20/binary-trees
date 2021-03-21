# Given the root of a binary tree and an integer targetSum, return true if the tree has a
# root - to - leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
# Example 1:
# Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
# Output: true
#
# Example 2:
# Input: root = [1, 2, 3], targetSum = 5
# Output: false
#
# Example 3:
# Input: root = [1, 2], targetSum = 0
# Output: false
#
# Constraints:
#
# The number of nodes in the tree is in the range[0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

from BinaryTrees import binary_tree


def has_path_sum(root, sum):
    def dfs(node, currsum):
        if node.left is None and node.right is None:
            if currsum == sum:
                return True
        if node.left and dfs(node.left, currsum + node.left.val):
            return True
        if node.right and dfs(node.right, currsum + node.right.val):
            return True
        return False

    if root is None:
        return False
    return dfs(root, root.val)


# def hasPathSum(root, targetSum):
#     if root is None:
#         return False
#
#     if not root.right and not root.left:
#         return root.val == targetSum
#
#     return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


t1 = binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
print(t1)
print(has_path_sum(t1, 22))
