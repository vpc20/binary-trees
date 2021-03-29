# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height - balanced binary search tree.
#
# A height - balanced binary tree is a binary tree in which the depth of the two subtrees of every
# node never differs by more than one.
#
# Example 1:
# Input: nums = [-10, -3, 0, 5, 9]
# Output: [0, -3, 9, -10, null, 5]
# Explanation: [0, -10, 5, null, -3, null, 9] is also
# accepted:
#
# Example 2:
# Input: nums = [1, 3]
# Output: [3, 1]
# Explanation: [1, 3] and [3, 1] are both a height - balanced BSTs.
#
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.
from BinaryTrees import TreeNode


def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    t = TreeNode(nums[mid])
    t.left = sorted_array_to_bst(nums[:mid])
    t.right = sorted_array_to_bst(nums[mid + 1:])
    return t


print(sorted_array_to_bst([1]))
print(sorted_array_to_bst([1, 3]))
print(sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7]))
