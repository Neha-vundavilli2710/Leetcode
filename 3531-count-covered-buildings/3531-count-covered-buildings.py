class Solution:
    def countCoveredBuildings(self, n, buildings):
        from collections import defaultdict
        from bisect import bisect_left
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        for k in rows:
            rows[k].sort()
        for k in cols:
            cols[k].sort()
        
        ans = 0
        
        for x, y in buildings:
            ys = rows[x]
            xs = cols[y]
            i = bisect_left(ys, y)
            j = bisect_left(xs, x)
            if i > 0 and i < len(ys) - 1 and j > 0 and j < len(xs) - 1:
                ans += 1
        
        return ans
