# Definition for a binary tree node.
'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode):
        to_left = False
        if not root: return []
        d = deque([root])
        result = []
        while d:
            s_arr = []
            s_len = len(d)
            for i in range(s_len):
                if to_left:
                    node = d.popleft()
                    s_arr.append(node.val)
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)
                else:
                    node = d.pop()
                    s_arr.append(node.val)
                    if node.left:
                        d.appendleft(node.left)
                    if node.right:
                        d.appendleft(node.right)
            to_left = not to_left
            result.append(s_arr)
        return result


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(4)
    t7 = TreeNode(1)
    t3.left = t4
    t3.right = t5
    t4.left = t1
    t5.right = t2
    print(s.levelOrder(t3))