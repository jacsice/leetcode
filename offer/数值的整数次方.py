class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n > 1:
            if n & 1:
                result *= x
                n -= 1
            else:
                x = x * x
                n = n // 2
            print(n)
        result *= x
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(0.01, 2147483647))