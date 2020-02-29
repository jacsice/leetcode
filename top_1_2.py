class Solution:
    # @param {integer[]} nums
    # 获取数据中的非重复的top1， top2
    def top_1_2(self, nums):
        top1 = 0
        top2 = 0
        for num in nums:
            if num > top1:
                top2, top1 = top1, num
            elif num > top2:
                top2 = num
        return top1, top2


if __name__ == '__main__':
    print(Solution().top_1_2([6,6,5,3,1,7,8]))