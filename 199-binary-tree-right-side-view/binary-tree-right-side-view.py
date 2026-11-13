# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        result = []
        
        def rev_post(node,level):
            if node is None :
                return 

            if len(result) == level :
                result.append(node.val)

            if node.right :
                rev_post(node.right, level + 1)

            if node.left :
                rev_post(node.left, level + 1)


        rev_post(root,0)
        return result


        
