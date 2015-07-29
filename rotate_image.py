#You are given an n x n 2D matrix representing an image.

#Rotate the image by 90 degrees (clockwise).

#Follow up:
#Could you do this in-place?

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        self.rotate_x(matrix)
        self.rotate_y(matrix)

    # 水平倒叙 
    # [1,2] --> [2,1]
    # [3,4]     [4,3]
    def rotate_x(self, matrix):
        m_len = len(matrix)
        for x in xrange(m_len):
            for i in xrange(m_len/2):
                matrix[x][i], matrix[x][m_len-i-1] = matrix[x][m_len-i-1], matrix[x][i]

    # 对角线对称交换 
    # [2,1] --> [3,1]
    # [4,3]     [4,2]
    def rotate_y(self, matrix):
        m_len = len(matrix) - 1
        for i in xrange(m_len):
            for j in xrange(m_len-i):
                matrix[i][j] ,matrix[m_len-j][m_len-i] = matrix[m_len-j][m_len-i], matrix[i][j]


# Time:  O(n^2)
# Space: O(n^2)
class Solution2:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
        
