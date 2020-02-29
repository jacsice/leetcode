class Solution:

    def __init__(self):
        self.results = set()
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def findWords(self, board, words):
        x_len = len(board)
        y_len = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        children = trie.children
        for i in range(x_len):
            for j in range(y_len):
                if board[i][j] in children:
                    self._dfs(board, i, j, x_len, y_len, '', children)

        return self.results

    def _dfs(self, board, i, j, x_len, y_len, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict.get(board[i][j], {})

        if 'is_end' in cur_dict:
            self.results.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'
        for index in range(4):
            x = i + self.dx[index]
            y = j + self.dy[index]
            if 0 <= x < x_len and 0 <= y < y_len and board[x][y] != '@' and board[x][y] in cur_dict:
                self._dfs(board, x, y, x_len, y_len, cur_word, cur_dict)
        board[i][j] = tmp


class Trie(object):
    def __init__(self):
        self.children = {}

    def insert(self, word):
        node = self.children
        for w in word:
            node.setdefault(w, {})
            node = node.get(w, {})
        node['is_end'] = True

    def search(self, word):
        node = self.children
        for w in word:
            if w not in node:
                return False
            node = node.get(w)
        return True


if __name__ == '__main__':
    words = ["abbbababaa"]
    board = [["b", "b", "a", "a", "b", "a"], ["b", "b", "a", "b", "a", "a"], ["b", "b", "b", "b", "b", "b"],
     ["a", "a", "a", "b", "a", "a"], ["a", "b", "a", "a", "b", "b"]]


    [""]

    solution = Solution()
    print(solution.findWords(board, words))
