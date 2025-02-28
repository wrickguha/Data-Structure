''' Given an encoded string s, the task is to decode it. The encoding rule is :

k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:

Input: s = "1[b]"
Output: "b"
Explanation: "b" is present only one time.
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
1. Inner substring “2[ca]” breakdown into “caca”.
2. Now, new string becomes “3[bcaca]”
3. Similarly “3[bcaca]” becomes “bcacabcacabcaca ” which is final result.  '''

class Solution:
    def decodedString(self, s):
        # code here
        
        stack = []

        for i in range(len(s)):
            
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr=""
                while stack[-1] != "[":
                    substr= stack.pop() + substr
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                    
                stack.append(int(k)*substr)
        
        return "".join(stack)



