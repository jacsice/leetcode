class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.nums_arr = [nums[0]]
        for i in range(1, len(nums)):
            self.nums_arr.append(self.nums_arr[i - 1] + nums[i])
        print(self.nums_arr)

    def sumRange(self, i: int, j: int) -> int:
        if i == j:
            return self.nums[i]
        if i == 0:
            return self.nums_arr[j]
        return self.nums_arr[j] - self.nums_arr[i-1]


if __name__ == '__main__':
    obj = NumArray([1,2,3,4,5])
    param_1 = obj.sumRange(1,3)
    print(param_1)