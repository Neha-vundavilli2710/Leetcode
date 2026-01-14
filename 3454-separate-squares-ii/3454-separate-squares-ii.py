class Solution:
    def separateSquares(self, squares):
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        
        def union_length(intervals):
            intervals.sort()
            total = 0
            cur_start, cur_end = -1, -1
            for s, e in intervals:
                if s > cur_end:
                    total += cur_end - cur_start
                    cur_start, cur_end = s, e
                else:
                    cur_end = max(cur_end, e)
            total += cur_end - cur_start
            return total

        slabs = []
        active = []
        prev_y = events[0][0]
        total_area = 0

        i = 0
        while i < len(events):
            y = events[i][0]
            height = y - prev_y
            if height > 0 and active:
                width = union_length(active)
                area = width * height
                slabs.append((prev_y, y, width, area))
                total_area += area

            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                i += 1
            prev_y = y

        half = total_area / 2
        curr = 0

        for y1, y2, width, area in slabs:
            if curr + area >= half:
                return y1 + (half - curr) / width
            curr += area

        return 0.0
