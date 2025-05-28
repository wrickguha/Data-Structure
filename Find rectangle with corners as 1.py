"""
Find rectangle with corners as 1
Difficulty: MediumAccuracy: 58.43%Submissions: 11K+Points: 4
Given an n x m binary matrix mat[][] containing only 0s and 1s, determine if there exists a rectangle within the matrix such that all four corners of the rectangle are 1. If such a rectangle exists, return true; otherwise, return false.

Example:

Input: mat[][] =
[[1, 0, 0, 1, 0],
[0, 0, 1, 0, 1],
[0, 0, 0, 1, 0], 
[1, 0, 1, 0, 1]] 
Output: true
Explanation: Valid corners are at index (1,2), (1,4), (3,2), (3,4) 
Input: mat[][] =
[[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
Output: false
Explanation: There are no valid corners.
Constraints:
1 <= n, m <= 200
0 <= mat[i] <= 1
"""


class Solution:    
    def ValidCorner(self, mat): 
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(i + 1, n):
                count = 0
                for col in range(m):
                    if mat[i][col] == 1 and mat[j][col] == 1:
                        count += 1
                        if count >= 2:
                            return True
        return False


