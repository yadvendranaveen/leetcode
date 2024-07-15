# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs(node):
            nonlocal ans
            if not node: return False

            left, right = dfs(node.left), dfs(node.right)
            mid = node==p or node==q

            if left+mid+right>=2:
                ans = node

            return left or right or mid
        
        dfs(root)
        return ans
        