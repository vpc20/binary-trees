from collections import deque
from itertools import chain
from random import shuffle, randint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        print_binary_tree(self)
        return ''

    def __repr__(self):
        return f'TreeNode({self.val})'

    def __len__(self):
        ctr = 0
        q = deque([self])
        while q:
            node = q.popleft()
            ctr += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ctr


def binary_tree(vals):
    """
     Create binary tree from level-order list of node values

     :param vals: list representation of binary tree
     :return: root of the tree
     """
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    root = nodes[0]
    for i, node in enumerate(nodes):
        if vals[i] is not None:
            l = i * 2 + 1
            if l < len(vals):
                node.left = nodes[l]
            r = i * 2 + 2
            if r < len(vals):
                node.right = nodes[r]
    return root


def binary_tree_values(node):
    """
     Return list of binary tree values in level-order sequence

     :param node: root of binary tree
     :return: list of values in level-order sequence
     """
    vals = []
    q = deque([node])
    while q:
        for _ in range(len(q)):  # process each level
            node = q.popleft()
            vals.append(node.val if node is not None else None)
            q.append(node.left if node is not None else None)
            q.append(node.right if node is not None else None)
        if set(q) == {None}:  # q contains all Nones
            break

    while len(vals) > 1 and vals[-1] is None:  # remove trailing Nones
        vals.pop()

    return vals


def binary_tree_nodes(node):
    """
     Return list of binary tree nodes in level-order sequence

     :param node: root of binary tree
     :return: list of nodes in level-order sequence
     """
    nodes = []
    q = deque([node])
    while q:
        for _ in range(len(q)):  # process each level
            node = q.popleft()
            nodes.append(node if node is not None else None)
            q.append(node.left if node is not None else None)
            q.append(node.right if node is not None else None)
        if set(q) == {None}:  # q contains all Nones
            break

    while len(nodes) > 1 and nodes[-1] is None:  # remove trailing Nones
        nodes.pop()

    return nodes


# def binary_tree_values(node):
#     height = tree_height(node)
#     h = 0
#     vals = []
#     q = deque([node])
#     while h <= height:
#         for _ in range(len(q)):
#             node = q.popleft()
#             if node is not None:
#                 vals.append(node.val)
#                 if node.left is not None:
#                     q.append(node.left)
#                 else:
#                     q.append(None)
#                 if node.right is not None:
#                     q.append(node.right)
#                 else:
#                     q.append(None)
#             else:
#                 vals.append(None)
#                 q.append(None)
#                 q.append(None)
#         h += 1
#
#     while len(vals) > 1 and vals[-1] is None:  # remove trailing Nones
#         vals.pop()
#
#     return vals


def print_preorder(root):
    def preorder(node):
        print(node.val, end=' ')
        if node.left is not None:
            preorder(node.left)
        if node.right is not None:
            preorder(node.right)

    preorder(root)
    print('')


def print_inorder(root):
    def inorder(node):
        if node.left is not None:
            inorder(node.left)
        print(node.val, end=' ')
        if node.right is not None:
            inorder(node.right)

    inorder(root)
    print('')


def print_postorder(root):
    def postorder(node):
        if node.left is not None:
            postorder(node.left)
        if node.right is not None:
            postorder(node.right)
        print(node.val, end=' ')

    postorder(root)
    print('')


def print_level_order(node):
    q = deque([node])
    while q:
        node = q.popleft()
        print(node.val, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print('')


def print_graphviz(node):
    print('digraph BST {')
    print('  node [shape=circle];')

    i = 0
    q = deque([node])
    while q:
        node = q.popleft()
        if node.left or node.right:
            if node.left:
                print(f'  {node.val} -> {node.left.val};')
            else:
                i += 1
                print(f'  n{i} [style=invis];')
                print(f'  {node.val} -> n{i} [style=invis];')

            i += 1
            print(f'  n{i} [style=invis];')
            print(f'  {node.val} -> n{i} [style=invis];')

            if node.right:
                print(f'  {node.val} -> {node.right.val};')
            else:
                i += 1
                print(f'  n{i} [style=invis];')
                print(f'  {node.val} -> n{i} [style=invis];')

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    print('}')


# def preorder_array(root):
#     def preorder(node):
#         arr.append(node.val)
#         if node.left:
#             preorder(node.left)
#         if node.right:
#             preorder(node.right)
#
#     arr = []
#     preorder(root)
#     return arr

def preorder_array(root):
    """
    Visit the root before the values in left and right subtree.

    :param root: root of the binary tree
    :return: preorder list of node values
    """
    if root is None:
        return []
    arr = [root.val]
    arr += preorder_array(root.left)
    arr += preorder_array(root.right)
    return arr


def preorder_array_iterative(node):
    """
    Visit the root before the values in left and right subtree.

    :param node: root of the binary tree
    :return: preorder list of node values
    """

    stack = [node]
    arr = []
    while stack:
        node = stack.pop()
        arr.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return arr


# def inorder_array(root):
#     def inorder(node):
#         if node.left:
#             inorder(node.left)
#         arr.append(node.val)
#         if node.right:
#             inorder(node.right)
#
#     arr = []
#     inorder(root)
#     return arr


def inorder_array(root):
    """
    Visit the root of a subtree between visiting the values in its left subtree and visiting those in its right
    subtree.

    :param root: root of the binary tree
    :return: inorder list of node values
    """
    if root is None:
        return []
    arr = inorder_array(root.left)
    arr += [root.val]
    arr += inorder_array(root.right)
    return arr


def inorder_array_iterative(node):
    """
    Visit the root of a subtree between visiting the values in its left subtree and visiting those in its right
    subtree.

    :param node: root of the binary tree
    :return: inorder list of node values
    """
    arr = []
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            arr.append(node.val)
            node = node.right
    return arr


# def postorder_array(root):
#     def postorder(node):
#         if node.left:
#             postorder(node.left)
#         if node.right:
#             postorder(node.right)
#         arr.append(node.val)
#
#     arr = []
#     postorder(root)
#     return arr


def postorder_array(root):
    """
    Visit the root after the values in left and right subtree.

    :param root: root of the binary tree
    :return: postorder list of node values
    """

    if root is None:
        return []
    arr = postorder_array(root.left)
    arr += postorder_array(root.right)
    arr += [root.val]
    return arr


def postorder_array_iterative(node):
    """
    Visit the root after the values in left and right subtree.

    :param node: root of the binary tree
    :return: postorder list of node values
    """

    stack = [node]
    arr = []
    while stack:
        node = stack.pop()
        arr.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return arr[::-1]


def level_order_array(node):
    """
    Visit every node on a level before going to a lower level.

    :param node: root of the binary tree
    :return: level-order list of node values
    """
    arr = []
    q = deque([node])
    while q:
        node = q.popleft()
        arr.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return arr


# def level_order_array_recursive(node):
#     """
#     Visit every node on a level before going to a lower level.
#
#     :param node: root of the binary tree
#     :return: level-order list of node values
#     """
#
#     def print_level(node, level):
#         if node:  # preorder walk, but print only the last level
#             if level == 0:
#                 arr.append(node.val)
#                 return
#             print_level(node.left, level - 1)
#             print_level(node.right, level - 1)
#
#     arr = []
#     for i in range(tree_height(node) + 1):
#         print_level(node, i)
#     return arr

def level_order_array_recursive(node):
    """
    Visit every node on a level before going to a lower level.

    :param node: root of the binary tree
    :return: level-order list of node values
    """

    def dfs(node, lvl):
        if lvl == len(levels):
            levels.append([node.val])
        else:
            levels[lvl].append(node.val)
        if node.left:
            dfs(node.left, lvl + 1)
        if node.right:
            dfs(node.right, lvl + 1)

    levels = []
    dfs(node, 0)
    return list(chain.from_iterable(levels))


def tree_height(node):
    """
    The height of a node in a tree is the number of edges on the longest simple downward path from the node to a leaf,
    and the height of a tree is the height of its root. The height of a tree is also equal to the largest depth of
    any node in the tree.

    :param node: node of the tree
    :return: height of the node
    """

    left = right = 0
    if node.left:
        left = 1 + tree_height(node.left)
    if node.right:
        right = 1 + tree_height(node.right)
    return max(left, right)


# noinspection PyTypeChecker
def print_binary_tree(node):
    if not node:
        print('There is no tree')
        return
    left_space = [48, 24, 12, 6, 3]
    space_bet_vals = [93, 45, 21, 9, 3]
    line_ctrs = [23, 11, 5, 2, 0]
    # left_space =     [384, 192,  96, 48, 24, 12, 6, 3]
    # space_bet_vals = [765, 381, 189, 93, 45, 21, 9, 3]
    # line_ctrs =      [191,  95,  47, 23, 11,  5, 2, 0]

    height = tree_height(node)
    lvl = 0
    left_idx = 4 - height
    spc_idx = 4 - height
    lnctr_idx = 4 - height
    lvlq = deque([node])
    q = deque([node])
    while q:
        print(' ' * left_space[left_idx], end='')
        left_idx += 1
        prev_lvlq = lvlq.copy()
        lvlq.clear()
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                print(str(node.val).center(3), end=' ' * space_bet_vals[spc_idx])
                if node.left:
                    q.append(node.left)
                    lvlq.append(node.left)
                else:
                    q.append(None)
                    lvlq.append(None)
                if node.right:
                    q.append(node.right)
                    lvlq.append(node.right)
                else:
                    q.append(None)
                    lvlq.append(None)
            else:
                q.append(None)
                lvlq.append(None)
                q.append(None)
                lvlq.append(None)
                print('   ', end=' ' * space_bet_vals[spc_idx])

        spc_idx += 1
        lvl += 1
        print('')
        if left_idx == len(left_space):
            break

        print(f' {" " * left_space[left_idx]}', end='')
        for i in range(len(prev_lvlq)):
            l = 2 * i
            r = 2 * i + 1
            if l < len(lvlq) and lvlq[l] and r < len(lvlq) and lvlq[r]:
                # full
                print(f'┌{"─" * line_ctrs[lnctr_idx]}┴{"─" * line_ctrs[lnctr_idx]}┐ ', end='')
            elif l >= len(lvlq) and r >= len(lvlq):
                # none
                print(f' {" " * line_ctrs[lnctr_idx]} {" " * line_ctrs[lnctr_idx]}  ', end='')
            elif not lvlq[l] and not lvlq[r]:
                # none
                print(f' {" " * line_ctrs[lnctr_idx]} {" " * line_ctrs[lnctr_idx]}  ', end='')
            elif l < len(lvlq) and lvlq[l]:
                # left
                print(f'┌{"─" * line_ctrs[lnctr_idx]}┘{" " * line_ctrs[lnctr_idx]}  ', end='')
            else:
                # right
                print(f' {" " * line_ctrs[lnctr_idx]}└{"─" * line_ctrs[lnctr_idx]}┐ ', end='')
            print(f'{" " * line_ctrs[lnctr_idx] * 2}', end='')
        print('')
        lnctr_idx += 1


def random_binary_tree():
    rndtbl = [500, 20, 20, 14, 14, 14, 14, 2, 2, 2, 2, 2, 2, 2, 2]
    n = 15
    vals = list(range(1, n + 1))
    shuffle(vals)

    for i in range(len(vals)):  # randomly change values to None
        x = randint(0, rndtbl[i])
        if not x:
            vals[i] = None

    for i in range(len(vals)):  # children of None should be updated to None
        if vals[i] is None:
            l = i * 2 + 1
            if l < len(vals):
                vals[l] = None
            r = i * 2 + 2
            if r < len(vals):
                vals[r] = None

    while len(vals) > 1 and vals[-1] is None:  # remove trailing Nones
        vals.pop()

    return binary_tree(vals)


if __name__ == '__main__':
    # t = binary_tree([1, 2, 3])
    # t = random_binary_tree()
    # print_binary_tree(t)
    # print(binary_tree_values(t))
    # bt = binary_tree([1, 2, 3])
    # print(binary_tree_values(bt))

    # bt = binary_tree([5, 4, 6, None, 0, 2, 3])
    # print(bt)
    # print(binary_tree_values(bt))
    # print(binary_tree_nodes(bt))
    # print(len(bt))

    bt = binary_tree([4, 2, 6, 1, 3, 5, 7])
    print(bt)
    print(postorder_array(bt))
    print(postorder_array_iterative(bt))
    # print(binary_tree_values(bt))
    # print(binary_tree_nodes(bt))
    # print(len(bt))
