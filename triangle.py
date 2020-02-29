class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        min = 0
        total = 0
        for arr in triangle:
            min = arr[0]
            for i in xrange(len(arr)):
                if arr[i] < min:
                    min = arr[i]
            total += min
        return total


class Solution2:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        
        cur = triangle[0] + [float("inf")]
        for i in range(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0])
            for j in range(1, i + 1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
            cur = next + [float("inf")]
            
        return reduce(min, cur)

if __name__ == "__main__":
    Solution2().minimumTotal([[-1], [2, 3], [1, -1, -3]])
            