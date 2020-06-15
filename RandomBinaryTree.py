from random import shuffle, randint
from binarytree import build
from BinaryTrees import binary_tree, print_preorder


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
    # print(vals)

    return binary_tree(vals), vals


if __name__ == '__main__':
    bt, vals = random_binary_tree()

    t = build(vals)
    print(t)

    for e in [e.val for e in t.preorder]:
        print(e, end=' ')
    print('')
    print_preorder(t)
