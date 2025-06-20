"""
Group Balls by Sequence
Difficulty: MediumAccuracy: 42.01%Submissions: 5K+Points: 4
You are given an array arr[] of positive integers, where each element arr[i] represents the number written on the i-th ball, and a positive integer k.
Your task is to determine whether it is possible to rearrange all the balls into groups such that:


Each group contains exactly k balls.
The numbers in each group are consecutive integers
Examples:

Input: arr[] = [10, 1, 2, 11], k = 2
Output: true
Explanation: The hand can be rearranged as [1, 2], [10, 11]. There are two groups of size 2. Each group has 2 consecutive cards.
Input: arr[] = [7, 8, 9, 10, 11], k = 2
Output: false
Explanation: The hand cannot be rearranged into groups of 2, since there are 5 cards, and 5 cards cannot be divided into groups of 2.
Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 105
1 ≤ k ≤ 103
"""

from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        n = len(arr)
        if n % k != 0:
            return False

        count = Counter(arr)
        sorted_keys = sorted(count.keys())

        for num in sorted_keys:
            while count[num] > 0:
                for i in range(num, num + k):
                    if count[i] == 0:
                        return False
                    count[i] -= 1

        return True
