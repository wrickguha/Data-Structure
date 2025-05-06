"""
Left View of Binary Tree
Difficulty: EasyAccuracy: 33.74%Submissions: 552K+Points: 2Average Time: 20m
You are given the root of a binary tree. Your task is to return the left view of the binary tree. The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.

If the tree is empty, return an empty list.

Examples :

Input: root[] = [1, 2, 3, 4, 5, N, N]

Output: [1, 2, 4]
Explanation: From the left side of the tree, only the nodes 1, 2, and 4 are visible.

Input: root[] = [1, 2, 3, N, N, 4, N, N, 5, N, N]

Output: [1, 2, 4, 5]
Explanation: From the left side of the tree, the nodes 1, 2, 4, and 5 are visible.

Input: root[] = [N]
Output: []
Constraints:
0 <= number of nodes <= 106
0 <= node -> data <= 105


"""


class Node:
    def __init__(self, data):  # Correct constructor
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def LeftView(self, root):
        if not root:
            return []

        result = []
        queue = [(root, 0)]
        max_level_seen = -1

        while queue:
            node, level = queue.pop(0)
            if level > max_level_seen:
                result.append(node.data)
                max_level_seen = level

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result

# Function to insert nodes in level-order to build a binary tree
def build_tree(elements):
    if not elements:
        return None

    root = Node(elements[0])
    queue = [root]
    i = 1

    while i < len(elements):
        current = queue.pop(0)
        if elements[i] is not None:
            current.left = Node(elements[i])
            queue.append(current.left)
        i += 1

        if i < len(elements) and elements[i] is not None:
            current.right = Node(elements[i])
            queue.append(current.right)
        i += 1

    return root


