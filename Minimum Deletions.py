"""
Minimum Deletions
Difficulty: MediumAccuracy: 58.8%Submissions: 64K+Points: 4
Given a string s, write a program to delete the minimum number of characters from the string so that the resultant string is a palindrome, while maintaining the order of characters.

Examples:

Input: s = "aebcbda"
Output: 2
Explanation: Remove characters 'e' and 'd'.
Input: s = "geeksforgeeks"
Output: 8
Explanation: To make "geeksforgeeks" a palindrome, the longest palindromic subsequence is "eefee" (length 5). The minimum deletions are:
13 (length of s) - 5 = 8.
Constraints:
1 ≤ s.size() ≤ 103
"""

class Solution:
    def minDeletions(self, s):
        n = len(s)
        rev_s = s[::-1]
        
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev_s[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev, curr = curr, [0] * (n + 1)  # Reuse array for next row
        
        # Minimum deletions = total length - length of LPS
        return n - prev[n]
