'''
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
'''


class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        x_len = len(matrix)
        y_len = len(matrix[0])

        i = x_len - 1
        j = 0
        while i >= 0 and j < y_len:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.findNumberIn2DArray([[1, 1]], 1))