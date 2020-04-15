'''
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
'''


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid: return 0
        x = len(grid)
        y = len(grid[0])
        max_count = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    count = self._dfs(grid, i, j, x, y) + 1
                    max_count = max(max_count, count)
        return max_count

    def _dfs(self, grid, i, j, x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        for direction in directions:
            i_next = direction[0] + i
            j_next = direction[1] + j
            print(i_next, j_next)
            if 0 <= i_next < x and 0 <= j_next < y and grid[i_next][j_next] == 1:
                grid[i_next][j_next] = 0
                print("====")
                count += 1 + self._dfs(grid, i_next, j_next, x, y)
        return count


if __name__ == '__main__':
    solution = Solution()
    grid = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    #print(solution.maxAreaOfIsland(grid))
    grid2 = [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 1, 1],
             [0, 0, 0, 1, 1]]
    #print(solution.maxAreaOfIsland(grid2))
    grid2 = [[1, 1]]
    print(solution.maxAreaOfIsland(grid2))
