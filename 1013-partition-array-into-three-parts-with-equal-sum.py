'''
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
'''


class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        sum_A = sum(A)
        target_num = sum_A // 3
        tmp = None
        count = 0
        for i in range(len(A)):
            if not tmp:
                tmp = 0
            tmp += A[i]
            if tmp == target_num and count != 2:
                count += 1
                tmp = None
        if tmp != target_num:
            return False
        return True


if __name__ == '__main__':
    print(Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
    print(Solution().canThreePartsEqualSum([1,-1,1,-1, 1, -1, 1, -1]))
    print(Solution().canThreePartsEqualSum([100, 1, -101, 0, 1, -1]))