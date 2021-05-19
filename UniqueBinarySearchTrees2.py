# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly
# n nodes of unique values from 1 to n. Return the answer in any order.
#
# Example 1:
# Input: n = 3
# Output: [[1, null, 2, null, 3], [1, null, 3, 2], [2, 1, 3], [3, 1, null, null, 2], [3, 2, null, 1]]
#
# Example 2:
# Input: n = 1
# Output: [[1]]
#
# Constraints:
# 1 <= n <= 8
from BinaryTrees import TreeNode


def generate_trees(n):
    def create_tree(node, nodes):
        # print(f'create_tree({nlist})')
        if not nodes:
            return None
        for i, node in enumerate(nodes):
            node.left = create_tree(node, nodes[:i])
            node.right = create_tree(node, nodes[i + 1:])
            print(node)
        return node

    nodes = []
    for i in range(1, n + 1):
        nodes.append(TreeNode(i))
    # print(nodes)

    t = create_tree(None, nodes)


print(generate_trees(3))

# node1a = TreeNode(1)
# node2a = TreeNode(2)
#
# node1b = TreeNode(1)
# node2b = TreeNode(2)
#
# node1a.right = node2a
# node2b.left = node1b
#
# return [node1a, node2b]
