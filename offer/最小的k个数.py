class Solution:
    def getLeastNumbers(self, arr, k: int):
        if not arr or k == 0:
            return []
        left = self.partition(arr, 0, len(arr) - 1) + 1
        if left == k:
            return arr[:left]
        elif left > k:
            return self.getLeastNumbers(arr[:left-1], k)
        else:
            return arr[:left] + self.getLeastNumbers(arr[left:], k - left)

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
        return left


if __name__ == '__main__':
    print(Solution().getLeastNumbers([0,0,1,2,4,2,2,3,1,4], 5))