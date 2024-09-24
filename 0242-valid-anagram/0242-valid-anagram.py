class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1=Counter(s)
        d2=Counter(t)
        if len(s)!=len(t):
            return False
        #for si in s:
         #   if si in d1:
          #      continue
           # d1[si]+=1
        
        print(d1)
        
        print(d2)
        for k,v in d1.items():
            if k not in d2:
                return False
            elif k in d2:
                if d2[k]!=d1[k]:
                    return False

        return True
