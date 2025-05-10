"""
Longest Subarray with Majority Greater than K
Difficulty: MediumAccuracy: 53.91%Submissions: 3K+Points: 4
Given an array arr[] and an integer k, the task is to find the length of longest subarray in which the count of elements greater than k is more than the count of elements less than or equal to k.

Examples:

Input: arr[] = [1, 2, 3, 4, 1], k = 2
Output: 3
Explanation: The subarray [2, 3, 4] or [3, 4, 1] satisfy the given condition, and there is no subarray of length 4 or 5 which will hold the given condition, so the answer is 3.
Input: arr[] = [6, 5, 3, 4], k = 2
Output: 4
Explanation: In the subarray [6, 5, 3, 4], there are 4 elements > 2 and 0 elements <= 2, so it is the longest subarray.
Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 106
0 <= k <= 106


"""

class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        max_len = 0
        index_map = {}  # maps prefix_sum to its first occurrence index

        for i in range(n):
            # Convert values
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            # If sum is positive from 0 to i, entire array is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # Store first occurrence of prefix_sum
                if prefix_sum not in index_map:
                    index_map[prefix_sum] = i
                # If prefix_sum - 1 exists, we found a subarray with net +1
                if (prefix_sum - 1) in index_map:
                    max_len = max(max_len, i - index_map[prefix_sum - 1])

        return max_len






