class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #[0,1][1,2],[2,3]
        indegree=defaultdict(int)
        outdegree=defaultdict(int)
        for src,des in paths:
            indegree[src]+=1
            indegree[des]-=1
        #print(indegree)
        #print(outdegree)
        indegree_sort=sorted(indegree.items(), key=lambda x:x[1])
        #print(indegree_sort)
        return "".join(indegree_sort[0][0])