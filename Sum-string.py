"""
Sum-string
Difficulty: HardAccuracy: 50.56%Submissions: 35K+Points: 8
Given a string s consisting of digits, determine whether it can be classified as a sum-string.

A sum-string is a string that can be split into two or more non-empty substrings such that:


The rightmost substring is equal to the sum of the two substrings immediately before it (interpreted as integers).

This condition must apply recursively to the substrings before it.

The rightmost substring (and any number in the sum) must not contain leading zeroes, unless the number is exactly '0'.

Examples:

Input: s = "12243660"
Output: true
Explanation: The string can be split as {"12", "24", "36", "60"} where each number is the sum of the two before it:
24 = 12 + 12, 36 = 12 + 24, and 60 = 24 + 36. Hence, it is a sum-string.
Input: s = "1111112223"
Output: true
Explanation: Split the string as {"1", "111", "112", "223"}, where:
112 = 1 + 111 and 223 = 111 + 112. Hence, it follows the sum-string rule.
Input: s = "123456"
Output: false
Explanation: There is no valid split of the string such that each part satisfies the sum-string property recursively.
Constraints:
1 <= s.size() <= 100
String consists of characters from '0' to '9'.
"""

class Solution:
    def isSumString(self, s):
        # Helper function to check the sum-string property recursively
        def is_valid_sum_string(s, first, second):
            sum_str = str(int(first) + int(second))
            # The next part of the string must match this sum
            if not s.startswith(sum_str):
                return False
            # If the matched sum is exactly the remaining string, it's valid
            if s == sum_str:
                return True
            # Recurse with the new values
            return is_valid_sum_string(s[len(sum_str):], second, sum_str)
        
        n = len(s)
        # Try all possible pairs of first and second numbers
        for i in range(1, n):  # first number ends at i-1
            for j in range(i+1, n):  # second number ends at j-1
                first = s[:i]
                second = s[i:j]
                # Skip if any has leading zeros (and is not '0')
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                if is_valid_sum_string(s[j:], first, second):
                    return True
        return False
