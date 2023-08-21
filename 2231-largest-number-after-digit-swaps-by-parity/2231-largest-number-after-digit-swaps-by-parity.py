class Solution:
    def largestInteger(self, num: int) -> int:
        odd=[]
        even=[]
        answer=""
        s=str(num)
        
        for i in range(len(s)):
            if int(s[i])%2==0:
                even.append(s[i])
            else:
                odd.append(s[i])
        odd.sort(reverse=True)
        even.sort(reverse=True)
        #print(odd)
        #print(odd[-1])
        i=0
        j=0
        
        for k in range(len(s)):
            if int(s[k])%2==0:
                answer=answer+even[i]
                i=i+1
            else:
                answer=answer+odd[j]
                j=j+1
               
            
        
        
        return int(answer)
        
        