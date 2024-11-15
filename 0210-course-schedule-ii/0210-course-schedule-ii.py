class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={}
        for i in range(numCourses):
            preMap[i]=[]
        
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        '''
        a course has 3 possible states:
        visited-> crs has been added to the output
        visited-> crs has not added to the output but to the cycle
        unvisited->crs has not been added to output or cycle
        '''
        output=[]
        visit,cycle=set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre)==False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True


        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return output