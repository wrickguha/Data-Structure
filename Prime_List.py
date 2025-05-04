"""
Prime List
Difficulty: MediumAccuracy: 53.68%Submissions: 28K+Points: 4
You are given the head of a linked list. You have to replace all the values of the nodes with the nearest prime number. If more than one prime number exists at an equal distance, choose the smallest one. Return the head of the modified linked list.

Examples :

Input: head = 2 → 6 → 10
Output: 2 → 5 → 11

Explanation: The nearest prime of 2 is 2 itself. The nearest primes of 6 are 5 and 7, since 5 is smaller so, 5 will be chosen. The nearest prime of 10 is 11.
Input: head = 1 → 15 → 20
Output: 2 → 13 → 19

Explanation: The nearest prime of 1 is 2. The nearest primes of 15 are 13 and 17, since 13 is smaller so, 13 will be chosen. The nearest prime of 20 is 19.
Constraints:
1 <= no. of Nodes <= 104
1 <= node.val <= 104


"""

class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def primeList(self, head):
        # code here
        current = head 
        while current:
            current.val = self.nearest_number(current.val)
            current = current.next
        return head

    def is_prime(self,num):
        if num<=1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num % i== 0:
                return False
        return True
        
    def nearest_number(self,n):
        
        if self.is_prime(n):
            return n
        
        lower = n-1
        upper = n+1
        while True:
            if self.is_prime(lower):
                return lower
            if self.is_prime(upper):
                return upper
            lower -= 1
            upper += 1