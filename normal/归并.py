
class Solution(object):
    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[0:mid])
        right = self.merge_sort(nums[mid:len(nums)])
        return self.merge(left, right)

    def merge(self, left_arr, right_arr):
        i = j = 0
        result = []
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] > right_arr[j]:
                result.append(right_arr[j])
                j += 1
            elif left_arr[i] < right_arr[j]:
                result.append(left_arr[i])
                i += 1
            else:
                result.append(left_arr[i])
                result.append(right_arr[j])
                i += 1
                j += 1
        if left_arr:
            result.extend(left_arr[i:])
        if right_arr:
            result.extend(right_arr[j:])
        return result


if __name__ == '__main__':
    l = [1, 5, 8, 1, 2, 4, 5]
    print(Solution().merge_sort(l))