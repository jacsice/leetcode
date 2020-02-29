class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.visited = set()
        i = j = 0
        return self._dfs(i, j, m, n, k)

    def _dfs(self, i, j, m, n, k):
        if self.pointSum(i) + self.pointSum(j) > k:
            return 0
        down = right = 0
        if i < m - 1 and (i + 1, j) not in self.visited:
            #self.visited.add((i+1, j))
            down = self._dfs(i + 1, j, m, n, k)
        if j < n - 1 and (i, j + 1) not in self.visited:
            #self.visited.add((i, j + 1))
            right = self._dfs(i, j + 1, m, n, k)
        return right + down + 1

    def pointSum(self, point):
        count = 0
        while point > 0:
            count += point % 10
            point //= 10
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(3, 2, 2))