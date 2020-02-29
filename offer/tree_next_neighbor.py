import math

class Tree(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def find_next(root, val):
    if not root:
        return
    root_arr = [root]
    index = 0
    for node in root_arr:
        if node.left:
            root_arr.append(node.left)
            if node.left.val == val:
                index = len(root_arr) - 1
        if node.right:
            root_arr.append(node.right)
            if node.right.val == val:
                index = len(root_arr) - 1

    if index + 1 < len(root_arr):
        if int(math.log(index+1, 2)) == int(math.log(index+2, 2)):
            return index + 1
    return


if __name__ == '__main__':
    root = Tree(0)
    node1 = Tree(1)
    node2 = Tree(2)
    node3 = Tree(3)
    node4 = Tree(4)
    node5 = Tree(5)
    node6 = Tree(6)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    print(find_next(root, 4))
