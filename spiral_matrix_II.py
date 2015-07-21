"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        value = 1
        x = 0
        y = 0
        results = [[0 for i in xrange(n)] for c in xrange(n)]
        if n > 0:
            count = (n*2-1)/4 + 1
            results[0][0] = 1
            for _ in xrange(count):
                while y < n-1 and results[x][y+1] == 0:
                    value += 1
                    y += 1
                    results[x][y] = value
                while x < n-1 and results[x+1][y] == 0:
                    value += 1
                    x += 1
                    results[x][y] = value
                while y > 0 and results[x][y-1] == 0:
                    value += 1
                    y -= 1
                    results[x][y] = value
                while x > 0 and results[x-1][y] == 0:
                    value += 1
                    x -= 1
                    results[x][y] = value
        return results
        
if __name__ == "__main__":
    print Solution().generateMatrix(3)