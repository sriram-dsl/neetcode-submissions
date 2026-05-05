"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_parent = set()
        a = p
        b = q

        while True: 
            if a is not None and b is not None and a.val == b.val : 
                return a
            if a is None : 
                a = p
            else : 
                a = a.parent
            if b is None : 
                b = q 
            else: 
                b = b.parent


        