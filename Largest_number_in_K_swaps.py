"""
Largest number in K swaps
Difficulty: MediumAccuracy: 18.84%Submissions: 112K+Points: 4Average Time: 30m
Given a number k and string s of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of s at most k times.

Examples :

Input: s = "1234567", k = 4
Output: 7654321
Explanation: Three swaps can make the input 1234567 to 7654321, swapping 1 with 7, 2 with 6 and finally 3 with 5.
Input: s = "3435335", k = 3
Output: 5543333
Explanation: Three swaps can make the input 3435335 to 5543333, swapping 3 with 5, 4 with 5 and finally 3 with 4.
Input: s = "1034", k = 2
Output: 4301
Explanation: Two swaps can make the input 1034 to 4301, swapping 1 with 4 and finally 0 with 3. 
Constraints:
1 ≤ s.size() ≤ 15
1 ≤ k ≤ 7


"""



class Solution:
    
    def findMaximumNum(self, s, k):
        self.max_num = s
        
        def helper(s_list, k, index):
            if k == 0 or index == len(s_list):
                return

            max_digit = max(s_list[index:])

            if max_digit != s_list[index]:
                # Only reduce k if we actually do a swap
                for j in range(len(s_list)-1, index-1, -1):
                    if s_list[j] == max_digit:
                        # Swap
                        s_list[index], s_list[j] = s_list[j], s_list[index]

                        current = ''.join(s_list)
                        if current > self.max_num:
                            self.max_num = current

                        # Recur with reduced k
                        helper(s_list, k-1, index+1)

                        # Backtrack
                        s_list[index], s_list[j] = s_list[j], s_list[index]
            else:
                helper(s_list, k, index+1)

        helper(list(s), k, 0)
        return self.max_num

