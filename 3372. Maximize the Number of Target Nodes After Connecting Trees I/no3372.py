from collections import defaultdict
from typing import List
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(node: int, p: int, c: List[List[int]], k: int) -> int:
            if k < 0:
                return 0
            res = 1
            for i in c[node]:
                if i == p:
                    continue
                res += dfs(i, node, c, k - 1)
            return res
        def build(edges: List[List[int]], k: int) -> List[int]:
            n = len(edges) + 1
            c = [[] for _ in range(n)]
            for u, v in edges:
                c[u].append(v)
                c[v].append(u)
            res = [0] * n
            for i in range(n):
                res[i] = dfs(i, -1, c, k)
            return res

        n = len(edges1) + 1
        c1 = build(edges1, k)
        c2 = build(edges2, k - 1)
        mc = max(c2)
        res = [c1[i] + mc for i in range(n)]
        return res