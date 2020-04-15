"""
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.max = 0
        self._dfs(root)
        return self.max

    def _dfs(self, head):
        if not head:
            return 0
        left = self._dfs(head.left)
        right = self._dfs(head.right)
        self.max = max(self.max, left+right)
        return max(left, right) + 1


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    print(Solution().diameterOfBinaryTree(t5))