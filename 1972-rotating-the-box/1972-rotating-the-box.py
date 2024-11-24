class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        trans_mat=[]
        #box
        m=len(box) #=1,ht
        n=len(box[0]) #=3,wid
        for i in range(len(box[0])):
            new_row=[]
            for row in box:
                new_row.append(row[i])
            trans_mat.append(new_row)    
        print(trans_mat)
        
        for i in range(n):
            trans_mat[i].reverse()

        print(trans_mat)
        #trans_mat
        #m=len(trans_mat)=3
        #n=len(trans_mat[0])=1
        for i in range(m):
            start=n-1
            for j in range(start,-1,-1):
                if trans_mat[j][i]=="*":
                    start=j-1
                elif trans_mat[j][i]=="#":
                    trans_mat[j][i]="."
                    trans_mat[start][i]="#"
                    start-=1

        return trans_mat