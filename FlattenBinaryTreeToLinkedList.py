# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points
# to the next node in the list and the left child pointer is always null.
#
# The "linked list" should be in the same order as a pre - order traversal of the binary tree.
#
# Example 1:
# Input: root = [1, 2, 5, 3, 4, null, 6]
# Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]
#
# Example 2:
# Input: root = []
# Output: []
#
# Example 3:
# Input: root = [0]
# Output: [0]
#
# Constraints:
# The number of nodes in the tree is in the range[0, 2000].
# -100 <= Node.val <= 100
#
# Follow up: Can you flatten the tree in -place( with O(1) extra space)?
from BinaryTrees import binary_tree, TreeNode


# def flatten(root):
#     """
#     Do not return anything, modify root in-place instead.
#     """
#
#     def preorder(node):
#         nonlocal head, curr
#         if node is None:
#             return
#         newnode = TreeNode(node.val)
#         curr.right = newnode
#         curr = newnode
#
#         preorder(node.left)
#         preorder(node.right)
#
#     if root is None:
#         return None
#
#     head = TreeNode()
#     curr = head
#     preorder(root)
#
#     root.right = head.right.right
#     root.left = None


# no extra space required
def flatten(root):
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
        return root
    nodes = []
    curr = root
    stack = [curr]
    while stack:
        curr = stack.pop()
        nodes.append(curr)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    print(nodes)
    for i in range(len(nodes) - 1):
        nodes[i].left = None
        nodes[i].right = nodes[i + 1]

    return root


t = binary_tree([1, 2, 5, 3, 4, None, 6])
t = binary_tree([1, 2, 5, 3, 4])
print(t)
print(flatten(t))  # print not working on level 6
