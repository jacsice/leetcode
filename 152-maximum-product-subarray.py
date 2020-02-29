class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        max_total = min_total = res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            max_total, min_total = max_total * num, min_total * num
            max_total, min_total = max(max_total, min_total, num), min(max_total, min_total, num)
            res = max_total if max_total > res else res
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))