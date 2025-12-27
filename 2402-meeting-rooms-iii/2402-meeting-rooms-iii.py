import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Sort meetings by start time
        meetings.sort()
        
        # Min-heap of available rooms
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # Min-heap of (endTime, room)
        used_rooms = []
        
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free rooms that are done before start
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(used_rooms, (end, room))
            else:
                prev_end, room = heapq.heappop(used_rooms)
                heapq.heapush = heapq.heappush
                heapq.heappush(used_rooms, (prev_end + duration, room))
            
            count[room] += 1
        
        # Return room with max meetings (tie → smallest index)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
