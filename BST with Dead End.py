"""
BST with Dead End
Difficulty: MediumAccuracy: 35.99%Submissions: 91K+Points: 4
You are given a Binary Search Tree (BST) containing unique positive integers greater than 0.

Your task is to determine whether the BST contains a dead end.

Note: A dead end is a leaf node in the BST such that no new node can be inserted in the BST at or below this node while maintaining the BST property and the constraint that all node values must be > 0.

Examples:

Input: root[] = [8, 5, 9, 2, 7, N, N, 1]

Output: true
Explanation: Node 1 is a Dead End in the given BST.
Input: root[] = [8, 7, 10, 2, N, 9, 13]

Output: true
Explanation: Node 9 is a Dead End in the given BST.
Constraints:
1 ≤ number of nodes ≤ 3000
1 ≤ node->data ≤ 105
"""

class Solution:
    def isDeadEnd(self, root):
        # Helper function to detect dead end
        def checkDeadEnd(node, min_val, max_val):
            if not node:
                return False
            
            # If min and max are equal, it's a dead end
            if min_val == max_val:
                return True
            
            # Recur for left and right subtrees with updated ranges
            left_dead_end = checkDeadEnd(node.left, min_val, node.data - 1)
            right_dead_end = checkDeadEnd(node.right, node.data + 1, max_val)
            
            return left_dead_end or right_dead_end

        return checkDeadEnd(root, 1, float('inf'))
