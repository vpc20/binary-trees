# Given the head of a singly linked list where elements are sorted in ascending order, convert it
# to a height balanced BST.
#
# For this problem, a height - balanced binary tree is defined as a binary tree in which the
# depth of the two subtrees of every node never differ by more than 1.
#
# Example 1:
# Input: head = [-10, -3, 0, 5, 9]
# Output: [0, -3, 9, -10, null, 5]
# Explanation: One possible answer is [0, -3, 9, -10, null, 5], which represents the shown
# height balanced BST.
#
# Example 2:
# Input: head = []
# Output: []
#
# Example 3:
# Input: head = [0]
# Output: [0]
#
# Example 4:
# Input: head = [1, 3]
# Output: [3, 1]
#
# Constraints:
# The number of nodes in head is in the range[0, 2 * 104].
# -10 ^ 5 <= Node.val <= 10 ^ 5

from BinaryTrees import TreeNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ''
        curr = self
        while curr:
            s += str(curr.val) + ' --> '
            curr = curr.next
        return s[:-5]


def linked_list(vals):
    if not vals:
        return None

    head = curr = ListNode(vals[0])
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def sorted_list_to_bst(head):
    def sorted_array_to_bst(nums):
        if not nums:
            return None
        mid = len(nums) // 2
        t = TreeNode(nums[mid])
        t.left = sorted_array_to_bst(nums[:mid])
        t.right = sorted_array_to_bst(nums[mid + 1:])
        return t

    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr.next
    return sorted_array_to_bst(nums)


l1 = linked_list([1, 2, 3, 4, 5, 6, 7])
print(l1)
print(sorted_list_to_bst(l1))
