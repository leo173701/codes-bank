class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = 0
        own =  -prices[0]
        for i,price in enumerate(prices):
            presell = sell
            preown = own
            sell = max(presell, preown - fee + price)  # 卖出
            own = max(preown, sell - price)            # 买进
        return sell