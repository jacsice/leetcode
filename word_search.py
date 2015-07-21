# Time:  O(m * n * l)
# Space: O(l)
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
# 
# For example,
# Given board =
# 
# [
#   "ABCE",
#   "SFCS",
#   "ADEE"
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
#


class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        road = []
        y = len(board[0])
        x = len(board)
        for i in xrange(x):
            for j in xrange(y):
                if board[i][j] == word[0]:
                    if self.locate(board, i, j, word, road, 0):
                        return True
                    else:
                        road = []
        return False
        
    def locate(self, board, i, j, word, road, count):
        if [i, j] in road:
            return False
        elif count == len(word):
            return True
            
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[count]:
            return False
            
        road.append([i, j])
        
        result = self.locate(board, i, j-1, word, road, count+1) or \
               self.locate(board, i+1, j, word, road, count+1) or \
               self.locate(board, i, j+1, word, road, count+1) or \
               self.locate(board, i-1, j, word, road, count+1)

        road.remove([i, j])
        return result

if __name__ == '__main__':
    board = [
                "ABCE",
                "SFES",
                "ADEE"]
    s = "ABCESEEEFS"
    print Solution().exist(board, s)
