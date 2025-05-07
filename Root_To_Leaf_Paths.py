"""
Root to Leaf Paths
Difficulty: MediumAccuracy: 43.65%Submissions: 139K+Points: 4Average Time: 30m
Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree.

Examples:

Input: root[] = [1, 2, 3, 4, 5, N, N]
ex-3
Output: [[1, 2, 4], [1, 2, 5], [1, 3]]
Explanation: All the possible paths from root node to leaf nodes are: 1 -> 2 -> 4, 1 -> 2 -> 5 and 1 -> 3
Input: root[] = [1, 2, 3]

Output: [[1, 2], [1, 3]] 
Explanation: All the possible paths from root node to leaf nodes are: 1 -> 2 and 1 -> 3
Input: root[] = [10, 20, 30, 40, 60, N, N]

Output: [[10, 20, 40], [10, 20, 60], [10, 30]]
Explanation: All the possible paths from root node to leaf nodes are: 10 -> 20 -> 40, 10 -> 20 -> 60 and 10 -> 30
Constraints:
1 <= number of nodes <= 104
1 <= node->data <= 104

"""


from typing import Optional
from collections import deque

from typing import List


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def Paths(self, root):
        # code here
        
        all_paths = []
        
        def dfs(node,path):
            if not node:
                return 
            path.append(node.data)
            
            if not node.left and not node.right:
                all_paths.append(path[:])
            else:
                dfs(node.left,path)
                dfs(node.right,path)
            path.pop()
            
        dfs(root,[])
        return all_paths