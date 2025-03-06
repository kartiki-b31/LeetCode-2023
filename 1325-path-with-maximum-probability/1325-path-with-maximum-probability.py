class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        n=len(edges)
        graph=defaultdict(list)
        for i in range(n):
            src=edges[i][0]
            des=edges[i][1]
            graph[src].append([des,succProb[i]])
            graph[des].append([src,succProb[i]])
        '''
        this is a priority queue, the PQ in python is just an array.
        Here, the key is -1 because we want a max heap.
        '''
        pq=[(-1,start_node)]
        visited=set()
        while pq:
            prob, cur=heapq.heappop(pq)
            visited.add(cur)

            if cur==end_node:
                return prob*(-1)
            for nei, edP in graph[cur]:
                if nei not in visited:
                    heapq.heappush(pq,(edP*prob,nei))
  
        return 0