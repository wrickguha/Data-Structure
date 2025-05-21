"""
Kth Smallest Number in Multiplication Table
Difficulty: HardAccuracy: 50.32%Submissions: 8K+Points: 8
Given three integers m, n and k. Consider a grid of m * n, where mat[i][j] = i * j (1 based index). The task is to return the kth smallest element in the m * n multiplication table.

Examples :

Input: m = 3, n = 3, k = 5
Output: 3
Explanation: 

The 5th smallest element is 3. 
Input: m = 2, n = 3, k = 6
Output: 6 
Explanation: [1, 2, 3][2, 4, 6]. The 6th smallest element is 6.
Constraints:
1 <= m, n <= 3 * 104
1 <= k <= m * n
"""

class Solution(object):
    def kthSmallest(self, m, n, k):
        def countLessEqual(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
