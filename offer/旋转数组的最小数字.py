'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
'''

class Solution:
    def minArray(self, numbers) -> int:
        if not numbers:
            return
        num_left = 0
        num_right = len(numbers) - 1
        while num_left < num_right:
            if numbers[num_left] < numbers[num_right]:
                return numbers[num_left]
            mid = (num_left + num_right) // 2
            print(num_left, mid, num_right)
            if numbers[mid] < numbers[num_right]:
                num_right = mid
            elif numbers[mid] == numbers[num_right]:
                num_left += 1
                num_right -= 1
            else:
                num_left = mid + 1
            print(num_left, mid, num_right)
        return numbers[num_left]


if __name__ == '__main__':
    s = Solution()
    print(s.minArray([10,1,10,10,10]))