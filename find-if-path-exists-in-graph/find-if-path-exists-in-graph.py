class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited=set()
        d=defaultdict(list)
        
        for ed in edges:
            d[ed[0]].append(ed[1])
            d[ed[1]].append(ed[0])
        #print(d)
        
        def bfs(v):
            q=[]
            q.append(v)
            while q:
                node=q.pop(0)
                if node not in visited:
                    for child in d[node]:
                        if child not in visited:
                            q.append(child)
                    visited.add(node)
                
        bfs(source)
        if destination not in visited:
            return False
            

        return True
