class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        n = len(colors)
        
        for i in range(1, n):
            # If two consecutive balloons have the same color
            if colors[i] == colors[i - 1]:
                # Remove the one with smaller time
                total_time += min(neededTime[i], neededTime[i - 1])
                # Keep the larger one’s time for next comparison
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        
        return total_time
