"""
Unique Paths in a Grid
Difficulty: MediumAccuracy: 50.47%Submissions: 39K+Points: 4
You are given a 2d list grid[][] of size n x m consisting of values 0 and 1.
A value of 0 means that you can enter that cell and 1 implies that entry to that cell is not allowed.
You start at the upper-left corner of the grid (1, 1) and you have to reach the bottom-right corner (n, m) such that you can only move in the right or down direction from every cell.
Your task is to calculate the total number of ways of reaching the target.

Note: The first (1, 1) and last (n, m) cell of the grid can also be 1.
It is guaranteed that the total number of ways will fit within a 32-bit integer.

Examples:

Input: n = 3, m = 3,
grid[][] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Output: 2
Explanation: There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Input: n = 1, m = 3,
grid[][] = [[1, 0, 1]]
Output: 0
Explanation: There is no possible path to reach the end.
Constraints:
1 ≤ n*m ≤ 106
"""

class Solution:
    def uniquePaths(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        # If start or end is blocked, return 0
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0

        dp = [[0 for _ in range(m)] for _ in range(n)]

        # Initialize the starting cell
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0  # Blocked cell
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]

        return dp[n-1][m-1]
