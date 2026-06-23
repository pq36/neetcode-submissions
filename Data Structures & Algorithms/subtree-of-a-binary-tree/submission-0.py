# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self,r,s):
        if r==None and s==None:
            return True
        if r==None or s==None:
            return False
        if r.val!=s.val:
            return False
        return self.check(r.right,s.right) and self.check(r.left,s.left) 
    def f(self,r,s):
        if self.check(r,s):
            return True
        if r==None:
            return False
        return self.f(r.right,s) or self.f(r.left,s)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.f(root,subRoot)