# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=deque()
        res=[]
        q.append(root)
        while q:
            n=len(q)
            r=[]
            for _ in range(n):
                el=q.popleft()
                r.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            res.append(r)
        return res
        