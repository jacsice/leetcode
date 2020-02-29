'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        res = 0
        max_profit = [[[0, 0] for j in range(3)] for i in range(len(prices))]
        max_profit[0][0], max_profit[0][1], max_profit[0][2] = 0, -prices[0], 0

        for i in range(1, len(prices)):
            max_profit[i][0] = max_profit[i-1][0]
            max_profit[i][1] = max(max_profit[i-1][1], max_profit[i-1][0]-prices[i])
            max_profit[i][2] = max_profit[i-1][1] + prices[i]
            res = max(res, max_profit[i][0], max_profit[i][1], max_profit[i][2])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1,2,4,2,5,7,2,4,9,0]))