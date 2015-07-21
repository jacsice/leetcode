class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        for i in xrange(len(nums)):
            if nums[i] < target:
                result = target - nums[i]
                if result in nums[i+1:]:
                    for j in xrange(i+1, len(nums)):
                        if nums[j] == result:
                            return [i+1, j+1]