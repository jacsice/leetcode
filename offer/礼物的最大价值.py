'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
示例 1:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
'''


class Solution:
    def maxValue(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        x_len = len(grid) - 1
        y_len = len(grid[0]) - 1
        for index in range(x_len-1, -1, -1):
            grid[index][y_len] += grid[index+1][y_len]
        for index in range(y_len-1, -1, -1):
            grid[x_len][index] += grid[x_len][index+1]
        for i in range(x_len-1, -1, -1):
            for j in range(y_len-1, -1, -1):
                grid[i][j] = max(grid[i][j]+grid[i][j+1], grid[i][j]+grid[i+1][j])
        return grid[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.maxValue([
        [1,2,5],
        [3,2,1],
    ]))