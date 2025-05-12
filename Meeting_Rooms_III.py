"""

Meeting Rooms III
Difficulty: HardAccuracy: 68.08%Submissions: 2K+Points: 8
You are given an integer n representing the number of rooms numbered from 0 to n - 1. Additionally, you are given a 2D integer array meetings[][] where meetings[i] = [starti, endi] indicates that a meeting is scheduled during the half-closed time interval [starti, endi). All starti values are unique.

Meeting Allocation Rules:

When a meeting starts, assign it to the available room with the smallest number.
If no rooms are free, delay the meeting until the earliest room becomes available. The delayed meeting retains its original duration.
When a room becomes free, assign it to the delayed meeting with the earliest original start time.
Determine the room number that hosts the most meetings. If multiple rooms have the same highest number of meetings, return the smallest room number among them.

Examples:

Input: n = 2, meetings[][] = [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]
Output: 1
Explanation: Time 0: Both rooms available. [0,6] starts in room 0.
Time 2: Room 0 busy until 6. Room 1 available. [2,3] starts in room 1.
Time 3: Room 1 frees up. [3,7] starts in room 1.
Time 4: Both rooms busy. [4,8] is delayed.
Time 6: Room 0 frees up. Delayed [4,8] starts in room 0 [6,10).
Time 6: [6,8] arrives but both rooms busy. It’s delayed.
Time 7: Room 1 frees up. Delayed [6,8] starts in room 1 [7,9).
Meeting counts: [2, 3]
Input: n = 4, meetings[][] = [[0, 8], [1, 4], [3, 4], [2, 3]
Output: 2
Explanation: Time 0: All rooms available. [0,8] starts in room 0.
Time 1: Room 0 busy until 8. Rooms 1, 2, 3 available. [1,4] starts in room 1.
Time 2: Rooms 0 and 1 busy. Rooms 2, 3 available. [2,3] starts in room 2.
Time 3: Room 2 frees up. [3,4] starts in room 2.
Meeting counts: [1, 1, 2, 0]
Constraints:

1 ≤ n ≤ 104
1 ≤ meetings.size() ≤ 104
meetings[i].size() == 2
0 ≤ starti < endi ≤ 104


"""


import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Sort meetings by start time
        meetings.sort()
        
        # Available rooms heap (sorted by room number)
        available = list(range(n))
        heapq.heapify(available)
        
        # Occupied rooms heap: (end_time, room_number)
        occupied = []
        
        # Count of meetings per room
        count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have become available by the current meeting's start time
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            
            duration = end - start
            
            if available:
                # Assign meeting to the lowest numbered available room
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                # Delay meeting until the next room is free
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (end_time + duration, room))
            
            count[room] += 1
        
        # Return the room with the maximum count (tie broken by smallest room number)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
