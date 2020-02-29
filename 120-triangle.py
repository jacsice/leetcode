class Solution:
    def minimumTotal(self, triangle):
        x_len = len(triangle)
        for x in range(x_len-2, -1, -1):
            for y in range(x+1):
                triangle[x][y] += min(triangle[x+1][y], triangle[x+1][y+1])
        return triangle[0][0]


if __name__ == '__main__':
    solution = Solution()
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(solution.minimumTotal(triangle))

