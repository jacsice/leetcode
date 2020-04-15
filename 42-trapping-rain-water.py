'''
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''
class Solution:
    def trap_1(self, height) -> int:
        # 动态编程
        ans = 0
        left_max = [height[0]] * len(height)
        right_max = [height[-1]] * len(height)
        for i in range(1, len(height)):
            left_max[i] = (max(left_max[i-1], height[i]))

        for i in range(len(height)-2, -1, -1):
            right_max[i] = (max(right_max[i+1], height[i]))

        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]
        print(ans)
        return ans

    def trap_2(self, height):
        # 栈
        stack = []
        cur = 0
        ans = 0
        while cur < len(height):
            while stack and height[cur] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if not stack:
                    break
                distance = cur - stack[-1] - 1
                h = min(height[stack[-1]], height[cur]) - height[top]
                ans = distance * h
            stack.append(cur)
            cur += 1
        print(ans)
        return ans

    def trap_3(self, height):
        # 双指针
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    arr = [5, 0, 1, 0, 3, 0, 6]
    s.trap_1(arr)
