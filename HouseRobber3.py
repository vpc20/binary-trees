from collections import deque

from BinaryTrees import binary_tree


# def rob(root):
#     def preorder(node, pred, accamt):
#         nonlocal maxamt
#         parent[node] = pred
#         if node is None:
#             maxamt = max(maxamt, accamt)
#             return
#         if parent[node] is None or parent[pred] is None:
#             accamt = node.val
#         else:
#             accamt += parent[parent[pred]].val
#         preorder(node.left, node, accamt)
#         preorder(node.right, node, accamt)
#
#     maxamt = 0
#     parent = {}
#     preorder(root, None, 0)
#     return maxamt


def rob(root):
    if root is None:
        return 0
    queue = deque([root])
    lvl = -1
    # lvlorder = []
    evenamt = 0
    oddamt = 0

    while queue:
        lvl += 1
        # lvlorder.append([])
        for _ in range(len(queue)):
            node = queue.popleft()
            # lvlorder[-1].append(node.val)
            if lvl % 2 == 0:
                evenamt += node.val
            else:
                oddamt += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    print(evenamt, oddamt)
    return max(evenamt, oddamt)


# t = binary_tree([4, 2, 6, 1, 3, 5, 7])
# t = binary_tree([3, 2, 3, None, 3, None, 1])
# t = binary_tree([3, 4, 5, 1, 3, None, 1])
t = binary_tree([4, 1, None, 2, None, None, None, 3])
print(t)
print(rob(t))
