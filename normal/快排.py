
class Solution(object):
    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        mid = self.partition(nums, left, right)
        self.quick_sort(nums, left, mid-1)
        self.quick_sort(nums, mid+1, right)

    def partition(self, nums, left, right):
        p = nums[left]
        while left < right:
            while left < right and nums[right] > p:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= p:
                left += 1
            nums[right] = nums[left]
        nums[right] = p
        print(nums)
        return left


if __name__ == '__main__':
    l = [5, 5, 8, 1, 2, 4, 5]
    print(Solution().quick_sort(l, 0, len(l)-1), l)