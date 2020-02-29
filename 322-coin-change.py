class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        return -1 if dp[amount] == float('inf') else dp[amount]




if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1,2,5], 11))