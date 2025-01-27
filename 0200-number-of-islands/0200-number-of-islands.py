from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])

        direc=[(0,1),(1,0),(0,-1),(-1,0)]
        
        def bfs(i,j,visited):
            q.append([i,j])
            
            while len(q)>0:
                [x,y]=q.popleft()

                if (x,y) not in visited:
                    visited.add((i,j))
                
                for dx,dy in direc:
                    nx=dx+x
                    ny=dy+y
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]=="1" and (nx,ny) not in visited:
                        q.append([nx,ny])
                        visited.add((nx,ny))
            return


        count=0
        visited=set()
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and (i,j) not in visited:
                    #q.append([i,j])
                    bfs(i,j,visited)
                    count+=1


        return count