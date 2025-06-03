"""
Substrings with K Distinct
Difficulty: MediumAccuracy: 20.46%Submissions: 161K+Points: 4Average Time: 20m
Given a string consisting of lowercase characters and an integer k, the task is to count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

Examples :

Input: s = "abc", k = 2
Output: 2
Explanation: Possible substrings are ["ab", "bc"]
Input: s = "aba", k = 2
Output: 3
Explanation: Possible substrings are ["ab", "ba", "aba"]
Input: s = "aa", k = 1
Output: 3
Explanation: Possible substrings are ["a", "a", "aa"]
Constraints:
1 ≤ s.size() ≤ 106
1 ≤ k ≤ 26
"""

class Solution:
    def countSubstr(self, s, k):
        # Helper function to count substrings with at most k distinct characters
        def atMostKDistinct(s, k):
            count = 0
            left = 0
            freq = {}
            
            for right in range(len(s)):
                char = s[right]
                freq[char] = freq.get(char, 0) + 1

                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1

                count += right - left + 1
            return count

        # Exactly k = At most k - At most (k - 1)
        return atMostKDistinct(s, k) - atMostKDistinct(s, k - 1)
