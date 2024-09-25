class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return None
        max_prof=0
        min_price=prices[0]

        for i in range(len(prices)):
            profit=prices[i]-min_price
            max_prof=max(profit,max_prof)
            min_price=min(min_price,prices[i])
        return max_prof