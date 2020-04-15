class Solution:
    def combinationSum(self, candidates, target: int):
        self.result = []
        self.dfs(candidates, target, [])
        print(self.result)

    def dfs(self, candidates, target, result):
        if target == 0:
            self.result.append(list(result))
            return
        elif target < 0:
            return
        for c in candidates:
            if target - c >= 0:
                if result and result[-1] > c:
                    continue
                result.append(c)
                self.dfs(candidates, target-c, result)
                result.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([2,3,4,5], 6))