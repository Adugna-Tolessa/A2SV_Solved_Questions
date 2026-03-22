# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.store = defaultdict(int)
        self.store[0] = 1
        self.cnt = 0
        def solve(root, currSum):
            if not root:
                return
            currSum += root.val
            self.cnt += self.store[currSum - targetSum]
            self.store[currSum] += 1

            solve(root.left,currSum)
            solve(root.right,currSum)
            self.store[currSum] -= 1
        solve(root, 0)
        return self.cnt