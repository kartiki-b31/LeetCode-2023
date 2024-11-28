class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        0 0 1 2 3 4 5 6
        0 0 1 1 1 1 1 1
        1 1 2 3 4 5 6 7
        2 1 3 6 10 15 21 28
        [[1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 3, 6, 10, 15, 21, 28]]
        '''

        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        #print(dp)
        return dp[m-1][n-1]
