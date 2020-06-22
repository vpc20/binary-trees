from BinaryTrees import binary_tree


def binary_tree_all_paths(node):
    def dfs(node, path):
        if len(path) > 1:
            paths.append(path)
        if node.left:
            dfs(node.left, path + [node.left.val])
        if node.right:
            dfs(node.right, path + [node.right.val])

    if node is None:
        return 0
    paths = []

    stack = [node]
    while stack:
        node = stack.pop()
        dfs(node, [node.val])
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return paths


t = binary_tree([1, 2, 3, 4, 5, 6, 7])
print(t)
print(binary_tree_all_paths(t))
