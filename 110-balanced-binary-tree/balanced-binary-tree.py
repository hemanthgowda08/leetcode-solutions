''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = vald   m 
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        
        def height (node) :
            if node is None :
                return 0
            
            lh = height(node.left)
            
            if lh == - 1:
                return -1
                
            rh = height(node.right)
            
            if rh == -1 :
                return -1
                
            if abs(lh - rh) > 1 :
                return - 1
                
            return max(lh,rh) + 1
                
                
        x = height(root)
        if x == -1 :
            return False
            
        return True
        
            
       