class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        for s,e in intervals:
            heapq.heappush(h, (e,0))
            heapq.heappush(h, (s,1))
        ans = 1
        temp = 0
        while h:
            time, isStart = heapq.heappop(h)
            if isStart:
                temp += 1
            else:
                temp -= 1
            ans = max(ans, temp)
        return ans
