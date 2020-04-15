class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        dp = [[False] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        max_s = s[0]
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    if j - i + 1 >= len(max_s):
                        max_s = s[i:j+1]
        return max_s


if __name__ == '__main__':
    print(Solution().longestPalindrome('ac'))
