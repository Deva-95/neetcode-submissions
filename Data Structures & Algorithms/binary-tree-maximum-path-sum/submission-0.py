# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(res,root):
            if not root : return 0

            left = max(0,dfs(res,root.left))
            right = max(0,dfs(res,root.right))
            res[0] = max(res[0],left+right+root.val)

            return max(left,right)+root.val
        
        res = [root.val]
        dfs(res,root)
        return res[0]