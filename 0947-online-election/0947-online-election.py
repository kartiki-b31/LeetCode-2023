from collections import defaultdict
class TopVotedCandidate:
    #d={0:}
    def __init__(self, persons: List[int], times: List[int]):
        self.winners = []
        self.times = times
        d = defaultdict(int)
        max_votes = 0
        winner = -1

        for i in range(len(persons)):
            d[persons[i]] += 1
            if d[persons[i]] >= max_votes:
                if d[persons[i]] > max_votes or persons[i] != winner:
                    winner = persons[i]
                max_votes = d[persons[i]]
            self.winners.append(winner)

    def q(self, t: int) -> int:
        
        l, r = 0, len(self.times) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.times[mid] == t:
                return self.winners[mid]
            elif self.times[mid] < t:
                l = mid + 1
            else:
                r = mid - 1
        return self.winners[r] 
        
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)