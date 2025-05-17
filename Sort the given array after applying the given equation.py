"""
Sort the given array after applying the given equation
Difficulty: MediumAccuracy: 36.21%Submissions: 16K+Points: 4
Given an integer array arr[] sorted in ascending order, along with three integers: A, B, and C. The task is to transform each element x in the array using the quadratic function A*(x2) + B*x + C. After applying this transformation to every element, return the modified array in sorted order.

Examples:

Input: arr[] = [-4, -2, 0, 2, 4], A = 1, B = 3, C = 5
Output: [3, 5, 9, 15, 33]
Explanation: After applying f(x) = 1*(x2)+ 3*x + 5 to each x, we get [9, 3, 5, 15, 33]. After sorting this array, the array becomes [3, 5, 9, 15, 33].
Input: arr[] = [-3, -1, 2, 4], A = -1, B = 0, C = 0
Output: [-16, -9, -4, -1]
Explanation: After applying f(x) = -1*(x2) + 0*x + 0 to each x, we get [ -9, -1, -4, -16 ]. After sorting this array, the array becomes  [-16, -9, -4, -1].
Constraints:
1 ≤ arr.size() ≤ 106
-103 ≤ arr[i], A, B, C ≤ 103

"""


class Solution:
    def sortArray(self, arr, A, B, C):
        def f(x):
            return A * x * x + B * x + C
        
        n = len(arr)
        result = [0] * n
        left, right = 0, n - 1
        
        # Fill from end if A > 0 (max at ends), else from beginning
        idx = n - 1 if A >= 0 else 0
        
        while left <= right:
            left_val = f(arr[left])
            right_val = f(arr[right])
            
            if A >= 0:
                if left_val > right_val:
                    result[idx] = left_val
                    left += 1
                else:
                    result[idx] = right_val
                    right -= 1
                idx -= 1
            else:
                if left_val < right_val:
                    result[idx] = left_val
                    left += 1
                else:
                    result[idx] = right_val
                    right -= 1
                idx += 1
        
        return result
