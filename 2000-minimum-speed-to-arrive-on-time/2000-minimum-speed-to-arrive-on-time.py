class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n=len(dist)
        def valid(dist,speed):
            time = 0.0
            for i in range(len(dist)):
                t = dist[i] / speed
                # Round off to the next integer, if not the last ride.
                
                if i == len(dist) - 1:
                    time += t 
                else:
                    time+=math.ceil(t)

            return time



        left, right = 1, int(1e7)
        min_speed = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Move to the left half.
            if valid(dist, mid) <= hour:
                min_speed = mid
                right = mid - 1
            else:
                # Move to the right half.
                left = mid + 1
        
        return min_speed
            
            