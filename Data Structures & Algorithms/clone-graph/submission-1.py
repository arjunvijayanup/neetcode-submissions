"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # Hashmap

        def clone(node):
            
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val) # Creating new Node() with value = old Node val
            oldToNew[node] = copy # Creating new hash map entry oldNode -> newNode
            for nei in node.neighbors: # Iterating through neiboughring nodes
                copy.neighbors.append(clone(nei)) 
            
            return copy
        
        return clone(node) if node else None

            