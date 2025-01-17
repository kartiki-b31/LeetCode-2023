class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts=Counter(s)
        #print(char_counts)
        #place most freq chars in even pos[0,2,4,6]
        maxi=0
        fre=""
        for key,val in char_counts.items():
            if val>maxi:
                maxi=val
                fre=key

        #print(fre)
        if maxi>math.ceil(len(s)/2):
            return ""
        ans=[""]*len(s)
        index=0
        while char_counts[fre]!=0:
            ans[index]=fre
            char_counts[fre]-=1
            index+=2
        #print(index)
        #very very smart wow just wow
        for char, count in char_counts.items():
            while count>0:
                if index>=len(s):
                    index=1
                ans[index]=char
                index+=2
                count-=1


        return "".join(ans)
        