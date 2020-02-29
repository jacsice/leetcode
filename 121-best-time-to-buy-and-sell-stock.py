'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
'''


class Solution:

    def maxProfit(self, prices) -> int:
        profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price
        return profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1,2,4,2,5,7,2,4,9,0]))