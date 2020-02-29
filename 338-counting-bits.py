class Solution:
    def countBits(self, num: int):
        result = []
        count = 0
        for i in range(num+1):
            if i == 0:
                result.append(0)
            elif i << 1 == 0:
                result.append(1)
                count = 1
            else:
                count += 1
                result.append(count)
        return result


if __name__ == "__main__":
    solution = Solution()
    for i in range(8):
        print(i, solution.countBits(i))