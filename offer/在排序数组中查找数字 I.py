'''
统计一个数字在排序数组中出现的次数。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
'''


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums: return 0
        lower = self.find_lower_bound(nums, target)
        upper = self.find_upper_bound(nums, target)
        print(upper, lower)
        return upper - lower

    def find_lower_bound(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def find_upper_bound(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.search([1], 1))