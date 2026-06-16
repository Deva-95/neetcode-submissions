# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def Sametree(p,q):
            if not p and not q:
                return True
            
            if (not p and q )or (not q and p):
                return False

            if p.val!=q.val:
                return False

            return Sametree(p.left,q.left) and Sametree(p.right,q.right)
        
        if not subroot:
            return True
        if not root:
            return False
        if Sametree(root,subroot):
            return True
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)