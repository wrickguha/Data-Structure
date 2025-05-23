"""
Dice throw
Difficulty: MediumAccuracy: 36.52%Submissions: 41K+Points: 4Average Time: 30m
Given n dice each with m faces. Find the number of ways to get sum x which is the summation of values on each face when all the dice are thrown.

Example:

Input: m = 6, n = 3, x = 12
Output: 25
Explanation: There are 25 total ways to get the Sum 12 using 3 dices with faces from 1 to 6.
Input: m = 2, n = 3, x = 6
Output: 1
Explanation: There is only 1 way to get the Sum 6 using 3 dices with faces from 1 to 2. All the dices will have to land on 2.
Constraints:
1 <= m,n,x <= 50
"""

class Solution:
    def noOfWays(self, m, n, x):
        # Initialize dp table
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case

        # Fill the table
        for dice in range(1, n + 1):
            for target in range(1, x + 1):
                for face in range(1, m + 1):
                    if target - face >= 0:
                        dp[dice][target] += dp[dice - 1][target - face]

        return dp[n][x]
