class Trie:

    def __init__(self, val=None):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.children
        for w in word:
            node.setdefault(w, {})
            node = node.get(w)
        node['is_end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.children
        for w in word:
            if w not in node:
                return False
            node = node.get(w, {})
        if node.get('is_end', False):
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.children
        for w in prefix:
            if w not in node:
                return False
            node = node.get(w, {})
        return True

    def __repr__(self):
        return str(self.val)


if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    obj.insert('bad')
    obj.insert('bottle')
    obj.insert('boot')
    obj.insert('applc')
    param_2 = obj.search('apple')
    param_3 = obj.startsWith('app')
    param_4 = obj.search('app')
    obj.insert('app')
    param_5 = obj.search('app')

    print(param_2, param_3, param_4, param_5)
