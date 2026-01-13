class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2

        def get_area_below(y):
            area = 0
            for _, yi, l in squares:
                if y <= yi:
                    continue
                if y >= yi + l:
                    area += l * l
                else:
                    area += l * (y - yi)
            return area

        low = min(s[1] for s in squares)
        high = max(s[1] + s[2] for s in squares)
        
        for _ in range(100):
            mid = (low + high) / 2
            if get_area_below(mid) < target:
                low = mid
            else:
                high = mid
                
        return low