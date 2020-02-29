'''
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = p3 = p5 = 0
        res = [1] * n
        for i in range(1, n):
            res[i] = min(res[p2]*2, res[p3]*3, res[p5]*5)
            if res[i] == res[p2]*2: p2 += 1
            if res[i] == res[p3]*3: p3 += 1
            if res[i] == res[p5]*5: p5 += 1
        return res[n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))