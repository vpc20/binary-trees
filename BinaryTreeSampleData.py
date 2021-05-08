from itertools import combinations, count

from BinaryTrees import binary_tree


def gen_subtrees(arr):
    def backtrack(arrx, r):
        if r == 0:
            arrx_copy = arrx.copy()
            for i in range(len(arrx_copy)):
                if arrx_copy[i] is None:  # if parent is None children should also be None
                    l = 2 * i + 1
                    if l < len(arrx_copy):
                        arrx_copy[l] = None
                    r = 2 * i + 2
                    if r < len(arrx_copy):
                        arrx_copy[r] = None
            if arrx_copy not in tree_arr:
                tree_arr.append(arrx_copy)
            return

        for i in range(1, len(arrx)):
            tmp = arrx[i]
            arrx[i] = None
            backtrack(arrx, r - 1)
            arrx[i] = tmp

    tree_arr = []
    for r in range(len(arr)):
        backtrack(arr.copy(), r)

    print(tree_arr)
    # replace None with 0 in sort key since None values cannot be sorted
    tree_arr.sort(key=lambda e: [item if item is not None else 0 for item in e])
    return tree_arr


def gen_subtrees1(arr):
    idxs = list(range(1, len(arr)))
    # print(idxs)
    tree_arr = []

    for r in range(len(arr)):
        for comb in combinations(idxs, r):
            arr_copy = arr.copy()
            for idx in comb:  # comb contains indices which will be replaced with None
                arr_copy[idx] = None
            for i in range(len(arr_copy)):
                if arr_copy[i] is None:  # if parent is None children should also be None
                    l = 2 * i + 1
                    if l < len(arr_copy):
                        arr_copy[l] = None
                    r = 2 * i + 2
                    if r < len(arr_copy):
                        arr_copy[r] = None
            if arr_copy not in tree_arr:  # remove duplicates
                tree_arr.append(arr_copy)

    # print(tree_arr)
    # replace None with 0 in sort key since None values cannot be sorted
    tree_arr.sort(key=lambda e: [item if item is not None else 0 for item in e])
    return tree_arr


def gen_subtrees2(arr):
    def backtrack(arrx, r):
        if r == 0:
            for e in prev:
                curr.append(e + arrx)
                print(e + arrx)
            return

        for i in range(len(arrx)):
            tmp = arrx[i]
            arrx[i] = None
            backtrack(arrx, r - 1)
            arrx[i] = tmp

    lo = 0
    hi = 0
    lvls = []
    curr = []
    prev = [[arr[0]]]
    result = [[arr[0]]]

    for i in count():  # separate each level
        l = 2 ** i  # length of each level
        hi = lo + l
        sl = arr[lo:hi]
        if sl:
            lvls.append(sl)
            lo = hi
        else:
            break

    for i in range(1, len(lvls)):
        curr = []
        for r in range(len(lvls[i])):
            backtrack(lvls[i].copy(), r)
        result += curr
        prev = curr.copy()

    return result

    # queue = deque([arr[0]])
    # lvls = []
    #
    # while queue:
    #     lvls.append([])
    #     count = len(queue)
    #     for _ in range(count):
    #         node = queue.popleft()
    #         lvls[-1].append(node.val)
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    # return lvls


arr = [4, 2, 6, 1, 3, 5, 7]  # level-order
# for vals in gen_subtrees(arr):
#     t = binary_tree(vals)
#     print(t)

for vals in gen_subtrees2(arr):
    t = binary_tree(vals)
    print(t)

# print(len(gen_subtrees2(arr)))
# print(gen_subtrees2([1, 2, 3, 4, 5]))
# print(gen_subtrees2([1, 2, 3, 4]))
# print(gen_subtrees2([1, 2, 3, 4, 5]))
# print(gen_subtrees2([1, 2, 3, 4, 5, 6, 7]))
