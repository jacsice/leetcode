class Solution:
    def findContinuousSequence(self, target: int):
        if target < 1: return []
        result = []
        i = 2
        total_sum = 1
        arr = [1]
        while arr:
            if total_sum < target:
                arr.append(i)
                total_sum += i
                i += 1
            elif total_sum > target:
                total_sum -= arr[0]
                arr = arr[1:]
            else:
                if len(arr) != 1:
                    result.append(arr)
                    total_sum -= arr[0]
                    arr = arr[1:]
                else:
                    break
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findContinuousSequence(9))