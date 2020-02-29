class Solution:
    def exist(self, board, word: str) -> bool:
        if not board:
            return False

        x_len = len(board)
        y_len = len(board[0])
        i = j = 0
        marked = [[False for _ in range(y_len)] for _ in range(x_len)]
        for i in range(x_len):
            for j in range(y_len):
                if self.find(board, word, 0, i, j, x_len, y_len, marked):
                    return True
        return False

    def find(self, board, word, index, i, j, x_len, y_len, marked):
        if index == len(word) - 1:
            return board[i][j] == word[index]
        if board[i][j] == word[index]:
            print(i, j)
            marked[i][j] = True
            if i + 1 < x_len and not marked[i+1][j]:
                if self.find(board, word, index+1, i+1, j, x_len, y_len, marked):
                    return True
            if i - 1 >= 0 and not marked[i-1][j]:
                if self.find(board, word, index+1, i-1, j, x_len, y_len, marked):
                    return True
            if j + 1 < y_len and not marked[i][j+1]:
                if self.find(board, word, index+1, i, j+1, x_len, y_len, marked):
                    return True
            if j - 1 >= 0 and not marked[i][j-1]:
                if self.find(board, word, index+1, i, j-1, x_len, y_len, marked):
                    return True
            marked[i][j] = False
        return False


if __name__ == '__main__':
    board =[
      ['A','B','F','D'],
      ['S','F','C','S'],
      ['F','C','E','E']
    ]
    solution = Solution()
    print(solution.exist(board, 'SFCFD'))