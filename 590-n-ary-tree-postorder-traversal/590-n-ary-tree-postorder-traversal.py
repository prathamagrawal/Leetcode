"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        results = []
        
        self.helper(root, results)
        
        return results
        
        
    def helper(self, root, results):
        if not root:
            return
        
        for child in root.children:
            self.helper(child, results)
            
        
        results.append(root.val)