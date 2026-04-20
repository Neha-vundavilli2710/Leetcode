class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        L=len(colors)        
        for i in range(L):
            if ( colors[i]!=colors[L-1] or 
                colors[~i]!=colors[0]):
                return L-1-i