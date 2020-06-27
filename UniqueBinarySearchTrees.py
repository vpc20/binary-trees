# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
from functools import lru_cache

from BinaryTrees import binary_tree


@lru_cache()
def num_trees(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += num_trees(i) * num_trees(n - 1 - i)
    return res


def num_trees_dyna(n):
    dp = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
            # print(f'dp[{i}] += dp[{j}] * dp[{i - j - 1}]')
            # print(f'{dp[i]} += {dp[j]} * {dp[i - j - 1]}')
    return dp[-1]


# 1, 1, 2, 5, 14, 42, 132, 429...
print(num_trees(3))
print(num_trees_dyna(4))
