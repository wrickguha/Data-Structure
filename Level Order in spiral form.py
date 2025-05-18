"""
Level Order in spiral form
Difficulty: EasyAccuracy: 36.43%Submissions: 220K+Points: 2Average Time: 20m
Given a binary tree and the task is to find the spiral order traversal of the tree and return the list containing the elements.
Spiral order Traversal mean: Starting from level 0 for root node, for all the even levels we print the node's value from right to left and for all the odd levels we print the node's value from left to right.
For below tree, function should return [1, 2, 3, 4, 5, 6, 7]

 

Examples:

Input: root = [1, 3, 2]
 
Output: [1, 3, 2]
Explanation: Start with root (1), print level 0 (right to left), then level 1 (left to right).
Input: root = [10, 20, 30, 40, 60]

Output: [10, 20, 30, 60, 40]
Explanation: Start with root (10), print level 0 (right to left), level 1 (left to right), and continue alternating.
Input: root = [1, 2, N, 4]
  
Output: [1, 2, 4]
Explanation: Start with root (1), then level 1 (left to right), then level 2 (right to left).
Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 105
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findSpiral(self, root):
        if not root:
            return []

        result = []
        s1 = [root]  # Stack for levels to be printed right to left
        s2 = []      # Stack for levels to be printed left to right

        while s1 or s2:
            # Print nodes from s1 and push children to s2
            while s1:
                node = s1.pop()
                result.append(node.data)
                # Push left then right to s2
                if node.right:
                    s2.append(node.right)
                if node.left:
                    s2.append(node.left)

            # Print nodes from s2 and push children to s1
            while s2:
                node = s2.pop()
                result.append(node.data)
                # Push right then left to s1
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)

        return result