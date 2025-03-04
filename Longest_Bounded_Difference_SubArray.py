'''
Longest Bounded-Difference Subarray
Difficulty: MediumAccuracy: 58.27%Submissions: 18K+Points: 4
Given an array of positive integers arr[] and a non-negative integer x, the task is to find the longest sub-array where the absolute difference between any two elements is not greater than x.
If multiple such subarrays exist, return the one that starts at the smallest index.

Examples: 

Input: arr[] = [8, 4, 2, 6, 7], x = 4 
Output: [4, 2, 6] 
Explanation: The sub-array described by index [1..3], i.e. [4, 2, 6] contains no such difference of two elements which is greater than 4.
Input: arr[] = [15, 10, 1, 2, 4, 7, 2], x = 5 
Output: [2, 4, 7, 2] 
Explanation: The sub-array described by indexes [3..6], i.e. [2, 4, 7, 2] contains no such difference of two elements which is greater than 5. 
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 109
0 <= x<= 109
'''

from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        n = len(arr)
        left = 0
        max_len = 0
        start_index = 0
        min_deque = deque()
        max_deque = deque()
        
        for right in range(n):
            while min_deque and arr[min_deque[-1]] > arr[right]:
                min_deque.pop()
            min_deque.append(right)
            
            while max_deque and arr[max_deque[-1]] < arr[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start_index = left
        
        return arr[start_index:start_index + max_len]


from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        n = len(arr)
        left = 0
        max_len = 0
        start_index = 0
        min_deque = deque()
        max_deque = deque()
        
        for right in range(n):
            while min_deque and arr[min_deque[-1]] > arr[right]:
                min_deque.pop()
            min_deque.append(right)
            
            while max_deque and arr[max_deque[-1]] < arr[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start_index = left
        
        return arr[start_index:start_index + max_len]

