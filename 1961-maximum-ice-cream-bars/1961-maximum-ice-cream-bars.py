class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n=len(costs)
        count=0
        sorted_costs=costs.sort()
        for i in range(n):
            if costs[i]<=coins:
                count+=1
                coins=coins-costs[i]
        return count
        