import heapq

class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()

        INF = 10**18
        dist = [[[INF]*(k+1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        idx = [0]*(k+1)
        pq = [(0, 0, 0, 0)]

        while pq:
            cost, i, j, t = heapq.heappop(pq)
            if cost > dist[i][j][t]:
                continue

            if i == m-1 and j == n-1:
                return cost

            if i+1 < m:
                nc = cost + grid[i+1][j]
                if nc < dist[i+1][j][t]:
                    dist[i+1][j][t] = nc
                    heapq.heappush(pq, (nc, i+1, j, t))

            if j+1 < n:
                nc = cost + grid[i][j+1]
                if nc < dist[i][j+1][t]:
                    dist[i][j+1][t] = nc
                    heapq.heappush(pq, (nc, i, j+1, t))

            if t < k:
                while idx[t+1] < len(cells) and cells[idx[t+1]][0] <= grid[i][j]:
                    _, x, y = cells[idx[t+1]]
                    if cost < dist[x][y][t+1]:
                        dist[x][y][t+1] = cost
                        heapq.heappush(pq, (cost, x, y, t+1))
                    idx[t+1] += 1

        ans = min(dist[m-1][n-1])
        return ans if ans < INF else -1
