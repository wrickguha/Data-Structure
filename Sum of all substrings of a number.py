"""
Sum of all substrings of a number
Difficulty: MediumAccuracy: 38.11%Submissions: 61K+Points: 4
Given an integer s represented as a string, the task is to get the sum of all possible sub-strings of this string.

Note: The number may have leading zeros.
It is guaranteed that the total sum will fit within a 32-bit signed integer.

Examples:

Input: s = "6759"
Output: 8421
Explanation:
Sum = 6 + 7 + 5 + 9 + 67 + 75 + 59 + 675 + 759 + 6759 = 8421
Input: s = "421"
Output: 491
Explanation: 
Sum = 4 + 2 + 1 + 42 + 21 + 421 = 491
Constraints:
1 <= |s| <= 9
"""

class Solution:
    def sumSubstrings(self, s):
        n = len(s)
        total_sum = 0
        prev_sum = 0

        for i in range(n):
            num = int(s[i])
            curr_sum = prev_sum * 10 + num * (i + 1)
            total_sum += curr_sum
            prev_sum = curr_sum

        return total_sum
