from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        list_counter=Counter(arr)
        #print(list_counter)
        new_arr=list(list_counter.values())
        
        
        #print(len(new_arr))
        #print(len(list(set(new_arr))))
        
        if len(new_arr)!=len(list(set(new_arr))):
            return False
        else:
            return True
            
        
        
        
        