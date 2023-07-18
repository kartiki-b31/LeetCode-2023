class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro=0
        minPrice=float("infinity")
        for i in range(len(prices)):
            if minPrice> prices[i]:
                minPrice=prices[i]
                
            maxPro=max(maxPro,prices[i]-minPrice)
            
        return maxPro