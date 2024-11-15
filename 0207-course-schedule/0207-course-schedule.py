class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={}
        for i in range(numCourses):
            preMap[i]=[]
        
        print(preMap)
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs]==[]:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        #1->2
        #3->4

        dfs(0)



        return True
