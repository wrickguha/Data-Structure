"""
Sum of nodes on the longest path
Difficulty: MediumAccuracy: 52.39%Submissions: 117K+Points: 4
Given a binary tree root[], you need to find the sum of the nodes on the longest path from the root to any leaf node. If two or more paths have the same length, the path with the maximum sum of node values should be considered.

Examples:

Input: root[] = [4, 2, 5, 7, 1, 2, 3, N, N, 6, N]
 
Output: 13
Explanation:

The highlighted nodes (4, 2, 1, 6) above are part of the longest root to leaf path having sum = (4 + 2 + 1 + 6) = 13
Input: root[] = [1, 2, 3, 4, 5, 6, 7]

Output: 11
Explanation: 

The longest root-to-leaf path is 1 -> 3 -> 7, with sum 11.
Copy to BlackBoxInput: root[] = [10, 5, 15, 3, 7, N, 20, 1]

Output: 19
Explanation: 

The longest root-to-leaf path is 10 -> 5 -> 3 -> 1 with a sum of 10 + 5 + 3 + 1 = 19.
Constraints:
1 <= number of nodes <= 106
0 <= node->data <= 104

"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def sumOfLongRootToLeafPath(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (length, sum)
            
            left_len, left_sum = dfs(node.left)
            right_len, right_sum = dfs(node.right)
            
            if left_len > right_len:
                return (left_len + 1, left_sum + node.data)
            elif right_len > left_len:
                return (right_len + 1, right_sum + node.data)
            else:
                return (left_len + 1, max(left_sum, right_sum) + node.data)

        return dfs(root)[1]
