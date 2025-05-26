"""
Insert in Sorted Circular Linked List
Difficulty: MediumAccuracy: 25.56%Submissions: 136K+Points: 4Average Time: 20m
Given a sorted circular linked list, the task is to insert a new node in this circular linked list so that it remains a sorted circular linked list.

Examples:

Input: head = 1->2->4, data = 2
Output: 1->2->2->4
Explanation: We can add 2 after the second node.

Input: head = 1->4->7->9, data = 5
Output: 1->4->5->7->9
Explanation: We can add 5 after the second node.

Constraints:
2 <= number of nodes <= 106
0 <= node->data <= 106
0 <= data <= 106
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node

        current = head

        # Case 2: Inserting before head (new smallest or largest)
        if data < head.data:
            # Find the last node to update its next pointer
            while current.next != head:
                current = current.next
            current.next = new_node
            new_node.next = head
            return new_node  # New head

        # Case 3: Insert in the middle or end
        current = head
        while current.next != head and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return head  # Head doesn't change
