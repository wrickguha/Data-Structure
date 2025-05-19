"""
Predecessor and Successor
Difficulty: MediumAccuracy: 47.36%Submissions: 139K+Points: 4
You are given root node of the BST and an integer key. You need to find the in-order successor and predecessor of the given key. If either predecessor or successor is not found, then set it to NULL.

Note:- In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than the target is the successor. 

Examples :

Input: root[] = [8, 1, 9, N, 4, N, 10, 3, N, N, N], key = 8

Output: 4 9
Explanation: In the given BST the inorder predecessor of 8 is 4 and inorder successor of 8 is 9.
Input: root[] = [10, 2, 11, 1, 5, N, N, N, N, 3, 6, N, 4, N, N], key = 11

Output: 10 -1
Explanation: In given BST, the inorder predecessor of 11 is 10 whereas it does not have any inorder successor.
Input: root[] = [2, 1, 3], key = 3

Output: 2 -1
Explanation: In given BST, the inorder predecessor of 3 is 2 whereas it does not have any inorder successor.
Constraints: 
1 <= no. of nodes <= 105
1 <= node->data <= 106
1 <= key <= 106

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findPreSuc(self, root, key):
        self.pre = None
        self.suc = None
        
        def helper(node):
            if not node:
                return
            
            if node.data == key:
                # Find predecessor: rightmost in left subtree
                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    self.pre = temp
                
                # Find successor: leftmost in right subtree
                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    self.suc = temp
                    
            elif key < node.data:
                self.suc = node
                helper(node.left)
            else:
                self.pre = node
                helper(node.right)
        
        helper(root)
        return (self.pre, self.suc)
