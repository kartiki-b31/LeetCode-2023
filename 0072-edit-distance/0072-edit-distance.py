class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ''' first string
            " " a b c d e f
    SS " "   0  1 2 3 4 5 6
        a    1  0 1 2 3 4 5
        z    2  1 1 2 3 4 5
        c    3  2 2 1 2 3 4
        d    4  3 3 2 1 2 3
        e    5  4 4 3 2 1 [2]
        
        FIRST STRING: abcde
        SECOND STRING azcde
        '''

        n, m = len(word1), len(word2) 
        #n=first,abcdef ,m=second,azcde
        inf = int(1e9+90)
        
        dp = [[inf for _ in range(n+1)] for _ in range(m+1)]
        #
        dp[0][0]=0
        for i in range(1,n+1):
            dp[0][i] = i
        #print(dp) # 0 1 2 3 4 5 6
        for i in range(1,m+1):
            dp[i][0] =  i
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[j-1]==word2[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = min(min(
                        dp[i-1][j] ,
                        dp[i][j-1] ),
                        dp[i-1][j-1]
                    )+1
                
        return dp[m][n]