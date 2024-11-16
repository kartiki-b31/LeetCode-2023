class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat) #rows
        n=len(mat[0]) #cols

        dir=0 #top-right==>0
        #dir=1 # bottom-left===1
        def flip(dir):
            if dir==0:
                return 1
            return 0
        
        res=[]
        def helper(dir,row,col):
            nonlocal res
            if row<0 or row>len(mat) or col<0 or col>len(mat[0]):
                return

            if len(res)==(n*m):
                return

            res.append(mat[row][col])
            #check top right.....mat[0][len(mat[0])-1]
            # if row, col is this dir==0 and then flip
            if dir==0 and row==0 and col==len(mat[0])-1:
                dir=flip(dir)
                helper(dir,row+1,col)
                
            #check bottom .....mat[len(mat)-1][0]
            #if row,col is this and dir==1 and then flip
            elif dir==1 and row==len(mat)-1 and col==0:
                dir=flip(dir)
                helper(dir,row,col+1)
                
            #check top.....mat[0][col]
            #if dir=0 then flip,row==0
            elif dir==0 and row==0:
                dir=flip(dir)
                helper(dir,row,col+1) #doubt how does hte column get incresed.
                return
            #check bottom....mat[len(mat)-1][col]
            #if row=len(mat)-1,dir==1 and flip
            elif dir==1 and row==len(mat)-1:
                dir=flip(dir)
                helper(dir,row,col+1)
                return
            #check left....mat[row][0]
            #if col==0, dir==1 and then flip
            elif dir==1 and col==0:
                dir=flip(dir)
                helper(dir,row+1,col)
                return
            #check right....mat[row][len(mat[0])-1]
            #if col===len(mat[0])-1, dir==0 then flip
            elif dir==0 and col==len(mat[0])-1:
                dir=flip(dir)
                helper(dir,row+1,col)
                return

            #if dir==0:
            #row-=1,col+=1
            if dir==0:
                helper(dir,row-1,col+1)
                return
            #if dir==1:
            #row+=1,col-=1
            elif dir==1:
                helper(dir,row+1,col-1)
                return
            return

        

        helper(0,0,0)
        return res