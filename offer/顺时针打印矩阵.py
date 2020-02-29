'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
'''


class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
            print(matrix)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))