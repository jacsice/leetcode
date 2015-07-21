#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. 
#The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?
#Above is a 3 x 7 grid. How many possible unique paths are there?
#Note: m and n will be at most 100.


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
     def uniquePaths(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                ways[j] += ways[j - 1]
        
        return ways[n - 1]


class Solution2:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        visited = {}
        for x in xrange(1, m+1):
            for y in xrange(1, n+1):
                visited["{}-{}".format(x, y)] = self.find(x, y, visited)

        return visited["{}{}".format(x, y)]

    def find(self, x, y, visited):
        key = "{}{}".format(x, y)
        if x == 1 or y == 1:
            return 1
        elif key in visited:
            return visited[key]
        else:
            return self.find(x-1, y, visited) + self.find(x, y-1, visited)
            

if __name__ == "__main__":
    #for i in xrange(1, 13):
    #    for j in xrange(1, 13):
    #        print "{}-{}".format(i ,j), Solution2().uniquePaths(i, j)
    #print Solution2().uniquePaths(10, 12)
    #print Solution2().uniquePaths(11, 11)
    print Solution().uniquePaths(100, 100)

        