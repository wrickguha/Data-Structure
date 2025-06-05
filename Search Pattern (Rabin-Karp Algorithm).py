"""
Search Pattern (Rabin-Karp Algorithm)
Difficulty: MediumAccuracy: 34.53%Submissions: 72K+Points: 4Average Time: 20m
Given two strings:

A text string in which you want to search.

A pattern string that you are looking for within the text.

Return all positions (1-based indexing) where the pattern occurs as a substring in the text. If the pattern does not occur, return an empty list.

All characters in both strings are lowercase English letters (a to z).

Examples:

Input: text = "birthdayboy", pattern = "birth"
Output: [1]
Explanation: The string "birth" occurs at index 1 in text.
Input: text = "geeksforgeeks", pattern = "geek"
Output: [1, 9]
Explanation: The string "geek" occurs twice in text, one starts are index 1 and the other at index 9.
Constraints:
1<= text.size() <=5*105
1<= pattern.size() <= text.size()
"""

class Solution:
    def search(self, pat, txt):
        # Prime number and base for hashing
        d = 256
        q = 101  # A prime number to reduce collisions

        M = len(pat)
        N = len(txt)
        result = []

        # Calculate the hash value of pattern and first window of text
        p = 0  # hash value for pattern
        t = 0  # hash value for txt
        h = 1

        # The value of h would be "pow(d, M-1)%q"
        for i in range(M - 1):
            h = (h * d) % q

        # Calculate the hash value of pattern and first window of text
        for i in range(M):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q

        # Slide the pattern over text one by one
        for i in range(N - M + 1):
            # Check the hash values of current window of text and pattern
            if p == t:
                # Check characters one by one
                if txt[i:i + M] == pat:
                    result.append(i + 1)  # 1-based index

            # Calculate hash value for next window of text
            # Remove leading digit, add trailing digit
            if i < N - M:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
                if t < 0:
                    t = t + q

        return result
