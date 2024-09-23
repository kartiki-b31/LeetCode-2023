class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix) #3 col
        n=len(matrix[0]) #4 rows
        '''
            [A]--->
        [B]1,3,5,7
        |10,11,16,20

        | 23,30, 34,60
        |
        

        def binarysearch(start,end):
            while start<=end:
                mid=(start+end)//2

        '''
        def binarySearch(matrix,target):
            start=0
            end=len(matrix)-1
            while start<=end:
                mid=(start+end)//2
                if matrix[mid]==target:
                    return True
                elif matrix[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            return False

        for i in range(m):
            if matrix[i][0]>target:
                break
            if matrix[i][-1]<target:
                continue
            else:
                res=binarySearch(matrix[i],target)
                return res
        return False


