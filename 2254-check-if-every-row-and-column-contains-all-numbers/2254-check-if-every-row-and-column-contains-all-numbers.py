class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        num_set=set()
        for i in range(1,n+1):
            num_set.add(i)
        
        for row in matrix:
            if set(row)!=num_set:
                return False
        
        transposed_mat=list(zip(*matrix))
        

        for col in transposed_mat:
            if set(col)!=num_set:
                return False

        return True