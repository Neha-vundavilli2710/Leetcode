import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        need = k - 1

        small = []   # max heap (store negatives)
        large = []   # min heap
        delayed = defaultdict(int)
        small_size = 0
        ssum = 0

        def prune(heap):
            while heap:
                x = heap[0]
                if delayed[x] > 0:
                    delayed[x] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal small_size, ssum
            if small_size > need:
                prune(small)
                x = -heapq.heappop(small)
                small_size -= 1
                ssum -= x
                heapq.heappush(large, x)
            elif small_size < need and large:
                prune(large)
                x = heapq.heappop(large)
                heapq.heappush(small, -x)
                small_size += 1
                ssum += x

        def add(x):
            nonlocal small_size, ssum
            if small_size < need:
                heapq.heappush(small, -x)
                small_size += 1
                ssum += x
            else:
                prune(small)
                if x < -small[0]:
                    y = -heapq.heappop(small)
                    ssum -= y
                    heapq.heappush(large, y)
                    heapq.heappush(small, -x)
                    ssum += x
                else:
                    heapq.heappush(large, x)
            balance()

        def remove(x):
            nonlocal small_size, ssum
            if x <= -small[0]:
                delayed[-x] += 1
                small_size -= 1
                ssum -= x
                prune(small)
            else:
                delayed[x] += 1
                prune(large)
            balance()

        for x in nums[1:dist+2]:
            add(x)

        ans = nums[0] + ssum

        for i in range(dist+2, n):
            remove(nums[i - (dist+1)])
            add(nums[i])
            ans = min(ans, nums[0] + ssum)

        return ans
