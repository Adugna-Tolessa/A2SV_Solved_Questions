# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not root.left and not root.right:
            return 1
        if not root.left: return r + 1
        if not root.right: return l + 1
        return min(l,r) + 1