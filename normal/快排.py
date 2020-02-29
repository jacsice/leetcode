
class Solution(object):
    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        mid = self.partition(nums, left, right)
        self.quick_sort(nums, 0, mid)
        self.quick_sort(nums, mid+1, right)

    def partition(self, nums, left, right):
        p = nums[left]
        while left < right:
            while left < right and nums[right] >= p:
                right -= 1
            while left < right and nums[right] < p:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        print(nums)
        return left


if __name__ == '__main__':
    l = [1, 5, 8, 1, 2, 4, 5]
    print(Solution().quick_sort(l, 0, len(l)-1))