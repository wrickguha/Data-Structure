"""
Count the paths
Difficulty: MediumAccuracy: 42.71%Submissions: 43K+Points: 4Average Time: 10m
Given a Directed Acyclic Graph (DAG) with V nodes labeled from 0 to V-1, and a list of directed edges, count the total number of distinct paths from a given start node to a destination node. Each edge is represented as edges[i] = [u, v], indicating a directed edge from u to v.

Examples :

Input: edges[][] = [[0,1], [0,3], [2,0], [2,1], [1,3]], V = 4, src = 2, dest = 3
Output: 3
Explanation: There are three ways to reach at 3 from 2. These are: 2 -> 1 -> 3, 2 -> 0 -> 3 and 2 -> 0 -> 1 -> 3.
Print-all-paths-1
Input: edges[][] = [[0,1], [1,2], [1,3], [2,3]], V = 4, src = 0, dest = 3
Output: 2
Explanation: There is two way to reach at 3 from 0 that is : 0 -> 1 -> 2 -> 3 and 0 -> 1 -> 3.
Print-all-paths-2
Constraints:
2  ≤  V  ≤  103
1  ≤   E = edges.size()  ≤  (V * (V - 1)) / 2
"""

class Solution:
    def countPaths(self, edges, V, src, dest):
        from collections import defaultdict

        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Step 2: Memoization dictionary
        memo = {}

        # Step 3: DFS with memoization
        def dfs(node):
            if node == dest:
                return 1
            if node in memo:
                return memo[node]

            total_paths = 0
            for neighbor in graph[node]:
                total_paths += dfs(neighbor)

            memo[node] = total_paths
            return total_paths

        return dfs(src)
