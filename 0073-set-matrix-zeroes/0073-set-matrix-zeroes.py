class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        row=[0]*n
        col=[0]*m

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    row[r]=1
                    col[c]=1

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if row[r] or col[c]:
                    matrix[r][c]=0
        