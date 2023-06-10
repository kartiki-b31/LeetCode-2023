class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans=0
        #print(len(grid[0]))
        for i in range(len(grid)):

            grid[i].sort(reverse=True)
            
        for i in range(len(grid[0])):
            empty_arr=[]
            for i in range(len(grid)):
                empty_arr.append(grid[i][0])
                del grid[i][0]
            ans=ans+max(empty_arr)





        return ans
        #grid[i].sort()
        #[4,2,1]
        #empty_arr[grid[i][0]]
        #del grid[i][0]
        #empty_arr=[4,3,1]

