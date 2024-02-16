from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        result=[]
        
        for s in strs:
            sorted_s=tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        
        for values in anagram_map.values():
            result.append(values)
            
        return result
        
        