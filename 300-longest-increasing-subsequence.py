class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        print(dp)
        return max(dp)

    def lengthOfLIS2(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                print(i, j, m, tails[m], num)
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
                print(i, j, m)
                print("========")
            tails[i] = num
            print("tail", tails)
            if j == res: res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS2([10,9,2,5,3,7,101,18]))