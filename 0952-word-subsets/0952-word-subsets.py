class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        flag_arr=[False]*len(words1)
        #print(flag_arr)
        for word in range(len(words1)):
            flag_arr[word]=False
            for letter in words2:
                if letter not in words1[word]:
                    flag_arr[word]=False
                    break
                flag_arr[word]=True
                

        #[f, True, True, True, True]
        #print(flag_arr)
        res=[]
        for i in range(len(flag_arr)):
            if flag_arr[i]==True:
                res.append(words1[i])
        #print(res)
        return res