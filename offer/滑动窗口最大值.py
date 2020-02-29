'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        from collections import deque
        if not nums: return []
        if k == 0: return []

        d = deque()
        left = 0
        right = 1
        result = []
        while right < len(nums):
            print("4444", d, result, left, right)
            if right - left + 1 <= k:
                if d and nums[right] > nums[d[0]]:
                    d.appendleft(right)
                else:
                    d.append(right)
                right += 1
                result.append(nums[d[0]])
                print("1111", d, result, left, right)
            else:
                left += 1
                print("2222", d, result, left, right)
                while left > d[0]:
                    d.popleft()
            print("33333", d, result, left, right)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))