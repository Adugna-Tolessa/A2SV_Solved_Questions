# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def solve(root, parent, gParent):
            if not root:
                return 0
                
            left = solve(root.left, root.val, parent)
            right = solve(root.right, root.val, parent)

            if gParent % 2:
                return left + right
            else:
                return left + right + root.val

        return solve(root, -1, -1)
