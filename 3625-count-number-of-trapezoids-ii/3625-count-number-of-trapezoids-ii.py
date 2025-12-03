from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)

        # cnt1: slope k -> dict of (intercept b -> count of segments)
        cnt1: dict[float, dict[float, int]] = defaultdict(lambda: defaultdict(int))
        # cnt2: encoded midpoint p -> dict of (slope k -> count of segments)
        cnt2: dict[int, dict[float, int]] = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1

                if dx == 0:
                    # vertical line: use big constant for slope, x1 as "intercept"
                    k = 1e9
                    b = float(x1)
                else:
                    # slope
                    k = dy / dx
                    # intercept computed with integer arithmetic first
                    b = (y1 * dx - x1 * dy) / dx

                # group by (k, b)
                cnt1[k][b] += 1

                # encode midpoint (x1 + x2, y1 + y2) into a single int key
                p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                cnt2[p][k] += 1

        ans = 0

        # add trapezoids: for each (k), do combinational sum over lines (different b)
        for e in cnt1.values():
            s = 0
            for t in e.values():
                ans += s * t
                s += t

        # subtract parallelograms counted twice: for each midpoint p, sum over slopes k
        for e in cnt2.values():
            s = 0
            for t in e.values():
                ans -= s * t
                s += t

        return ans