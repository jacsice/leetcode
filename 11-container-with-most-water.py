class Solution:

    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def maxArea_1(self, height) -> int:
        dp = [0] * len(height)
        for i in range(1, len(height)):
            for j in range(0, i):
                dp[i] = max(dp[i-1], min(height[i], height[j])*(i-j), dp[i])
        return dp[-1]


if __name__ == '__main__':
    l = [1, 5, 8, 1, 2, 4, 5]
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))