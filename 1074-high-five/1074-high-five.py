import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        '''
        #[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],
        '''
        scores=defaultdict(list)
        for ids, score in items:
            heapq.heappush(scores[ids],score)
            if len(scores[ids])>5:
                heapq.heappop(scores[ids])

        results=[]
        for ids in sorted(scores.keys()):
            total_avg=sum(scores[ids])//5
            results.append([ids,total_avg])

        return results