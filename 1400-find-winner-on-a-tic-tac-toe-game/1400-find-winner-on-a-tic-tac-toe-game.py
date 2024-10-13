class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0] * 3 for _ in range(3)] 
        
        for i in range(len(moves)):
            if i%2==0: #i=2
                grid[moves[i][0]][moves[i][1]]="X" #[0,1]
            elif i%2!=0:
                grid[moves[i][0]][moves[i][1]]="O"
        
        print(grid)
        
        def checkcol(i):
            j=0
            if grid[j][i]=="X":
                while j<3:
                    if grid[j][i]!="X":
                        break
                    j+=1
                if j==3:
                    return True,"X"
                else:
                    return False,"0"
            elif grid[j][i]=="O":
                while j<3:
                    if grid[j][i]!="O":
                        break
                    j+=1
                if j==3:
                    return True,"O"
                else:
                    return False,"0"
            else:
                return False,"0"

        def checkrow(i):
            j=0
            if grid[i][j]=="X":
                while j<3:
                    if grid[i][j]!="X":
                        break
                    j+=1
                if j==3:
                    return True,"X"
                else:
                    return False,"0"
            elif grid[i][j]=="O":
                while j<3:
                    if grid[i][j]!="O":
                        break
                    j+=1
                if j==3:
                    return True,"O"
                else:
                    return False,"0"
            else:
                return False,"0"
        def checkleftdiag(sym):
            if grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2]:
                return True
            else:
                return False
        def checkrightdiag(sym):
            if grid[2][0]==grid[1][1] and grid[1][1]==grid[0][2]:
                return True
            else:
                return False

        #print(checkcol(0))
        #print(checkrow(0))
        if grid[0][0]=="X":
            if checkleftdiag("X"):
                print("me")
                return "A"
        

        if grid[0][0]=="O":
            if checkleftdiag("O"):
                print("try")
                return "B"

            
        if grid[0][2]=="X":
            if checkrightdiag("X"):
                print("inside")
                return "A"
           

        if grid[0][2]=="O":
            if checkrightdiag("O"):
                print("iam")
                return "B"
        
        for i in range(3):
            anscol,vari=checkcol(i)
            if anscol:
                if vari=="X":
                    print("onit")
                    return "A"
                elif vari=="O":
                    return "B"
        
        for i in range(3):
            ansrow,vari=checkrow(i)
            if ansrow:
                if vari=="X":
                    print("onit")
                    return "A"
                elif vari=="O":
                    return "B"

        len_m=len(moves)
        if len(moves)==9:
            return "Draw"
        else:
            return "Pending"
