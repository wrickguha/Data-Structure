"""
Print leaf nodes from preorder traversal of BST
Difficulty: MediumAccuracy: 47.26%Submissions: 31K+Points: 4
Given a preorder traversal of a BST, find the leaf nodes of the tree without building the tree.


Examples:

Input: preorder[] = [5, 2, 10]
Output: [2, 10]
Explaination: 

2 and 10 are the leaf nodes as shown in the figure.
Input: preorder[] = [4, 2, 1, 3, 6, 5]
Output: [1, 3, 5]
Explaination: 

1, 3 and 5 are the leaf nodes as shown in the figure.
Input: preorder[] = [8, 2, 5, 10, 12]
Output: [5, 12]
Explaination: 

5 and 12 are the leaf nodes as shown in the figure.

Constraints:
1 ≤ preorder.size() ≤ 103
1 ≤ preorder[i] ≤ 103
"""

class Solution:
    def leafNodes(self, preorder):
        n = len(preorder)
        self.index = 0
        res = []

        def helper(mini, maxi):
            if self.index >= n:
                return None

            val = preorder[self.index]

            if val < mini or val > maxi:
                return None

            self.index += 1

            # If this is a leaf, both left and right calls return None
            left = helper(mini, val - 1)
            right = helper(val + 1, maxi)

            if left is None and right is None:
                res.append(val)

            return True  # indicates that the node exists

        helper(float('-inf'), float('inf'))
        return res
