class Solution:

    def permutation(self, s: str):
        self.result = set()
        for index, c in enumerate(s):
            self.dfs(s, c, set([index]))
        return list(self.result)

    def dfs(self, s, c, visited):
        if len(s) == len(c):
            self.result.add(c)
            return
        for index, _c in enumerate(s):
            if index not in visited:
                visited.add(index)
                self.dfs(s, c + _c, visited)
                visited.remove(index)


if __name__ == '__main__':
    s = Solution()
    print(s.permutation('aab'))