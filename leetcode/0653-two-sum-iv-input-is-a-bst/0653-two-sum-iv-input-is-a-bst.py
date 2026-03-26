# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        store = set()
        def solve(root):
            if not root: return False
            if root.val in store:
                return True
            store.add(k - root.val)
            if solve(root.left): return True
            if solve(root.right): return True
            return False
        return solve(root)