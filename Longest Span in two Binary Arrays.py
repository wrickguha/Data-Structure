"""
Longest Span in two Binary Arrays
Difficulty: MediumAccuracy: 48.22%Submissions: 14K+Points: 4
Given two binary arrays, a1[] and a2[]. Find the length of longest common span (i, j) where j>= i such that a1[i] + a1[i+1] + .... + a1[j] =  a2[i] + a2[i+1] + ... + a2[j].

Examples:

Input: a1[] = [0, 1, 0, 0, 0, 0], a2[] = [1, 0, 1, 0, 0, 1]
Output: 4
Explanation: The longest span with same sum is from index 1 to 4 following zero based indexing.
Input: a1[] = [0, 1, 0, 1, 1, 1, 1], a2[] = [1, 1, 1, 1, 1, 0, 1]
Output: 6
Explanation: The longest span with same sum is from index 1 to 6 following zero based indexing.
Constraints:
1 <= a1.size() = a2.size() <= 106
0 <= a1[i], a2[i] <= 1
"""

class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff = [a1[i] - a2[i] for i in range(n)]

        prefix_sum = 0
        max_len = 0
        sum_index_map = {}

        for i in range(n):
            prefix_sum += diff[i]

            # If prefix_sum is 0, longest subarray from 0 to i
            if prefix_sum == 0:
                max_len = i + 1

            # If prefix_sum has been seen before, calculate subarray length
            if prefix_sum in sum_index_map:
                length = i - sum_index_map[prefix_sum]
                max_len = max(max_len, length)
            else:
                # Store first occurrence of the prefix_sum
                sum_index_map[prefix_sum] = i

        return max_len
