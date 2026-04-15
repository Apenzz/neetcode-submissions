class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax, r = 0, 0
        for l in range(1, len(prices)):
            currMax = max(currMax, prices[l] - prices[r])
            if prices[l] <= prices[r]:
                r = l
        return currMax