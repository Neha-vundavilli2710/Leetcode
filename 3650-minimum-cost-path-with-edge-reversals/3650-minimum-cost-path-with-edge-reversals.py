import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n, edges):
        adj = defaultdict(list)
        radj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            radj[v].append((u, w))

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in adj[u]:
                nc = cost + w
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))

            for v, w in radj[u]:
                nc = cost + 2 * w
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))

        return dist[n - 1] if dist[n - 1] != INF else -1
