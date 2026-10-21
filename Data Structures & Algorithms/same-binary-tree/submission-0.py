# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

#in such situation of edge cases like 1 or 0 , 1 and 0 check we always go for and because if botha are false then its already returning the false rather than true


        
        