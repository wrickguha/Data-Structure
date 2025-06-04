"""
LCS of three strings
Difficulty: MediumAccuracy: 48.52%Submissions: 77K+Points: 4
Given three strings s1, s2, and s3 containing uppercase letters, lowercase letters, and digits, find the length of longest common sub-sequence in all three given strings.

Examples:

Input: s1 = "geeks", s2 = "geeksfor", s3 = "geeksforgeeks"
Output: 5
Explanation: "geeks"is the longest common subsequence with length 5.
Input: s1 = "abcd1e2", s2 = "bc12ea", s3 = "bd1ea"
Output: 3
Explanation:  Longest common subsequence is "b1e" i.e. length = 3.
Constraints:
1  ≤  s1.size(), s2.size(), s3.size()  ≤  100
"""

class Solution:
    def lcsOf3(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        # Create a 3D DP table initialized to 0
        dp = [[[0] * (n3 + 1) for _ in range(n2 + 1)] for __ in range(n1 + 1)]

        # Fill the DP table
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
        
        # Final answer
        return dp[n1][n2][n3]