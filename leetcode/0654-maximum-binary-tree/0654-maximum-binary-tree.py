# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(nums):
            idx = nums.index(max(nums))
            node = TreeNode(nums[idx])
            if len(nums[idx + 1:]) > 0:
                node.right = solve(nums[idx + 1:])
            if len(nums[:idx]) > 0:
                node.left = solve(nums[:idx])
            return node
        return solve(nums)