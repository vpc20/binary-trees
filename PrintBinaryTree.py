from collections import deque
from binarytree import build

from BinaryTrees import binary_tree
from HeightOfATree import tree_height
from RandomBinaryTree import random_binary_tree


def print_binary_tree(node):
    left_space = [48, 24, 12, 6, 3]
    space_bet_vals = [93, 45, 21, 9, 3]
    line_ctrs = [23, 11, 5, 2, 0]

    height = tree_height(node)
    lvl = 0
    left_idx = 4 - height
    spc_idx = 4 - height
    lnctr_idx = 4 - height
    lvlq = deque([node])
    prev_lvlq = deque()
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

    print('')


# print(
#     '0         1         2         3         4         5         6         7         8         9         10        11 '
#     '       12        13')
# print(
#     '0....+....0....+....0....+....0....+....0....+....0....+....0....+....0....+....0....+....0....+....0....+....0'
#     '....+....0....+....0..')

# t = binary_tree([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
# print_binary_tree(t)

# t = binary_tree(list(range(1, 32)))
# print_binary_tree(t)
#
# t = binary_tree(list(range(1, 16)))
# print_binary_tree(t)
#
# t = binary_tree(list(range(1, 8)))
# print_binary_tree(t)
#
# t = binary_tree(list(range(1, 4)))
# print_binary_tree(t)
#
# t = binary_tree([1])
# print_binary_tree(t)

t, vals = random_binary_tree()
print(vals)
print_binary_tree(t)

# t1 = binary_tree([5, None, 14, None, None, 4, 3, None, None, None, None, None, 12, 7])
# t1 = binary_tree([5, None, 14, None, None, None, 3])
# print_binary_tree(t1)

# t2 = build([5, None, 14, None, None, 4, 3, None, None, None, None, None, 12, 7])
# print(t2)
# 5_____
#       \
#     ___14__
#    /       \
#   4         3
#    \       /
#     12    7


# t2 = build([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
# print(t2)
