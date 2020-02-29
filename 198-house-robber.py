class Solution:
    def rob(self, nums) -> int:
        prevMax = 0
        currMax = 0
        for x in nums:
            prevMax, currMax = currMax, max(prevMax + x, currMax)
        return currMax


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([2,4,8,9,9,3]))
