class Solution:
    def maxArea(self, height: List[int]) -> int:
        wid=1
        ht=1
        area=wid*ht
        maxarea=0
        left=0
        right=len(height)-1
        print(right)
        while left<=right: #0, 8
            wid=right-left #8
            #ht_diff=abs(height[right]-height[left]) #6
            ht=min(height[right],height[left]) #1
            area=wid*ht #8
            #print(wid)
            #print(ht)
            if area>maxarea:
                maxarea=area
            #print(maxarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
    
        
        return maxarea
            