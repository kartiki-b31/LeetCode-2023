class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res=[]
        tempDict=Counter()
        #bitwiseOR, takes the union of both the counters
        for w in words2:
            tempDict|=Counter(w)
        
        for w in words1:
            if not tempDict-Counter(w):
                res.append(w)
        print(tempDict)

        return res