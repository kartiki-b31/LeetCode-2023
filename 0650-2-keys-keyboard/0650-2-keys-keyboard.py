class Solution:
    def minSteps(self, n: int) -> int:
        '''
        n=3
        output=AAA
        nUMBEROF OPERATIONS: LEN((1)+(2)+(2))
        n=9:
        output=9As
        noofoperations:len(1,2,2,1,2,2)=6
        A
        1: A
        2: AA
        2: AAA
        1: AAA
        2: AAAAAA
        2: AAAAAAAAA

        or
        1: A
        2: AA
        1: AA
        2: AAAA
        2: AAAAAA 
        1: str.add("cur_str")
        2: 

        '''
        count=0
        current_len=1
        copy_len=0
        maxi=float('inf')
        memo={}
        def dfs(current_len,copy_len,count):#(3,1,3),(6,3,5)
            if (current_len,copy_len) in memo:
                return memo[(current_len,copy_len)]
            if current_len==n:
                return count

            if current_len>n:#n=9,3>9
                return maxi

            copy_paste=dfs(2*current_len,current_len,count+2)#6,3,5
            #print(copy_paste,"copy-paste")
            #print(current_len,"current_len")
            paste=float('inf')
            if copy_len!=0:
                paste=dfs(current_len+copy_len,copy_len,count+1)#(3,1,3),(9,3,6)
            #print(paste,"paste")
            #print(copy_len,"copy_len")
            memo[(current_len,copy_len)]=min(copy_paste,paste)
            return memo[(current_len,copy_len)]
            

        return dfs(1,0,0)
        