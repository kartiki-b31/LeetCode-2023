class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n<=1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])
        new_inte=intervals[0]
        res=[]
        res.append(new_inte)
        for inte in intervals:
            if inte[0]<=new_inte[1]:
                new_inte[1]=max(new_inte[1],inte[1])
            else:
                new_inte=inte
                res.append(new_inte)
        
        return res
            