class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m=len(rooms)
        if m==0:
            return
        n=len(rooms[0])
        if n==0:
            return
        dire=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        q=[]
        def bfs(i,j):
            q.append([i,j])
            while q:
                x,y=q.pop(0)
                cand_dist=rooms[x][y]+1
            
                for dx,dy in dire:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<m and 0<=ny<n and rooms[nx][ny] > cand_dist:
                        rooms[nx][ny]=cand_dist
                        q.append((nx,ny))

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    bfs(i,j)
        