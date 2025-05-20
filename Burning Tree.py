"""
Burning Tree
Difficulty: HardAccuracy: 53.53%Submissions: 109K+Points: 8
Given a binary tree and a target node, determine the minimum time required to burn the entire tree if the target node is set on fire. In one second, the fire spreads from a node to its left child, right child, and parent.
Note: The tree contains unique values.

Examples : 

Input: root[] = [1, 2, 3, 4, 5, 6, 7], target = 2
  
Output: 3
Explanation: Initially 2 is set to fire at 0 sec 
At 1 sec: Nodes 4, 5, 1 catches fire.
At 2 sec: Node 3 catches fire.
At 3 sec: Nodes 6, 7 catches fire.
It takes 3s to burn the complete tree.
Input: root[] = [1, 2, 3, 4, 5, N, 7, 8, N, 10], target = 10

Output: 5
Explanation: Initially 2 is set to fire at 0 sec 
At 1 sec: Node 5 catches fire.
At 2 sec: Node 2 catches fire.
At 3 sec: Nodes 1 and 4 catches fire.
At 4 sec: Node 3 and 8 catches fire.
At 5 sec: Node 7 catches fire.
It takes 5s to burn the complete tree.
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105


"""


class Solution:
    def minTime(self, root, target):
        from collections import deque, defaultdict

        # Step 1: Build parent map and find target node
        parent = {}
        target_node = None

        def dfs(node, par):
            nonlocal target_node
            if not node:
                return
            if node.data == target:
                target_node = node
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Step 2: BFS to simulate burning process
        visited = set()
        queue = deque()

        queue.append(target_node)
        visited.add(target_node)

        time = -1  # Start from -1 because the first level is at time = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for nei in (curr.left, curr.right, parent[curr]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            time += 1

        return time

