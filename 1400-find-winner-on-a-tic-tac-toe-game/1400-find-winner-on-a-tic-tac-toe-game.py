class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid=[[""]*3 for i in range(3)]
        for i in range(len(moves)):
            if i%2==0:
                grid[moves[i][0]][moves[i][1]]="A"
            elif i%2!=0:
                grid[moves[i][0]][moves[i][1]]="B"
        
        print(grid)

        if grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]!="":
            return grid[0][0]
        if grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]!="":
            return grid[1][0]
        if grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]!="":
            return grid[2][0]
        if grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]!="":
            return grid[0][0]
        if grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]!="":
            return grid[0][1]
        if grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]!="":
            return grid[0][2]
        if grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]!="":
            return grid[0][0]
        if grid[0][2]==grid[1][1]==grid[2][0] and grid[0][2]!="":
            return grid[0][2]
            

        if len(moves)==9:
            return "Draw"
        else:
            return "Pending"
