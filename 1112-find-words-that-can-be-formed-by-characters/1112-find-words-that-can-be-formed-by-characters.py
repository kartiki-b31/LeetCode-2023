class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d1=defaultdict(int)
        for si in chars:
            d1[si]+=1
        
        res=set()
        anss=0
        for word in words:
            d2=defaultdict(int)
            for c in word:
                d2[c]+=1
            
            flag=True
            for c in word:
                if d2[c]>d1[c]:
                    flag=False
                    break
            if flag:
                anss+=len(word)
        
        print(res)
        ans=set()
        ans=set(words)-res
        print(ans)
        lens=0
        for s1 in ans:
            lens+=len(s1)


        return anss
                
