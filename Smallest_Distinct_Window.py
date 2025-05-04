"""
Smallest distinct window
Difficulty: MediumAccuracy: 31.85%Submissions: 102K+Points: 4
Given a string str, your task is to find the length of the smallest window that contains all the characters of the given string at least once.

Example:

Input: str = "aabcbcdbca"
Output: 4
Explanation: Sub-String "dbca" has the smallest length that contains all the characters of str.
Input: str = "aaab"
Output: 2
Explanation: Sub-String "ab" has the smallest length that contains all the characters of str.
Input: str = "geeksforgeeks"
Output: 8
Explanation: There are multiple substring with smallest length that contains all characters of str, "geeksfor" and "forgeeks". 
Constraints:
1 ≤ str.size() ≤ 105
str contains only lower-case english alphabets.


"""


class Solution:
    def findSubString(self, str):
        n = len(str)
        if n == 0:
            return 0

        # Count all distinct characters in the string
        distinct_chars = set(str)
        total_distinct = len(distinct_chars)

        freq_map = {}
        min_len = n + 1
        start = 0
        count = 0

        for end in range(n):
            char = str[end]
            freq_map[char] = freq_map.get(char, 0) + 1

            if freq_map[char] == 1:  # new unique char in window
                count += 1

            # Try to shrink the window
            while count == total_distinct:
                min_len = min(min_len, end - start + 1)

                # Remove the start character
                freq_map[str[start]] -= 1
                if freq_map[str[start]] == 0:
                    count -= 1
                start += 1

        return min_len