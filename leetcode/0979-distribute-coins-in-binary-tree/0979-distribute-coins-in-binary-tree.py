# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def solve(curr):
            if not curr: return 0
            l = solve(curr.left)
            r = solve(curr.right)
            extra = curr.val - 1 + l + r
            self.ans += abs(extra)
            return extra
        solve(root)
        return self.ans