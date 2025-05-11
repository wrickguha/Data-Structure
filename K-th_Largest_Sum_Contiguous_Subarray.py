"""
K-th Largest Sum Contiguous Subarray
Difficulty: MediumAccuracy: 54.33%Submissions: 24K+Points: 4Average Time: 20m
Given an array arr[] of size n, find the sum of the K-th largest sum among all contiguous subarrays. In other words, identify the K-th largest sum from all possible subarrays and return it.

Examples:

Input: arr[] = [3, 2, 1], k = 2 
Output: 5
Explanation: The different subarray sums we can get from the array are = [6, 5, 3, 2, 1]. Where 5 is the 2nd largest.
Input: arr[] = [2, 6, 4, 1], k = 3
Output: 11
Explanation: The different subarray sums we can get from the arrayare = [13, 12, 11, 10, 8, 6, 5, 4, 2, 1]. Where 11 is the 3rd largest.
Constraints:
1 <= arr.size() <= 1000
1 <= k <= (n*(n+1))/2
-105 <= arr[i] <= 105
"""

from typing import List
import heapq

class Solution:
    def kthLargest(self, arr: List[int], k: int) -> int:
        n = len(arr)
        subarray_sums = []

        # Generate all contiguous subarray sums
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += arr[j]
                subarray_sums.append(sum_)

        # Sort all subarray sums in descending order
        subarray_sums.sort(reverse=True)

        # Return the K-th largest sum
        return subarray_sums[k - 1]





