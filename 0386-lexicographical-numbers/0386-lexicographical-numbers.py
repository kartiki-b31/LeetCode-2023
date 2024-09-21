class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr=[]
        for i in range(1,n+1):
            arr.append(str(i))
        
        arr.sort()
        #print(arr)
        int_arr=[]
        for i in range(n):
            int_arr.append(int(arr[i]))
        #print(int_arr)

        return int_arr