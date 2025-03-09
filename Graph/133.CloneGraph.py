"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q, clones = deque([node]), {node.val: Node(node.val)}

        while q:
            curr = q.popleft()
            clone = clones[curr.val]

            for neighbor in curr.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                clone.neighbors.append(clones[neighbor.val])
            
        return clones[node.val]

# Time: O(V+E) 
# Space: O(V+E)