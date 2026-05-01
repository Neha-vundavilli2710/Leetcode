import numpy as np
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = np.array([c for row in grid for c in row])
        med = np.partition(arr, len(arr)//2)[len(arr)//2]
        return  int(np.abs(arr-med).sum())//x if np.all((arr %x) == (arr[0] %x)) else -1