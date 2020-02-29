# Definition for a binary tree node.
'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        self.result = []
        self._dfs(root, 0, '', sum)
        return self.result

    def _dfs(self, root, total_sum, val_str, sum):
        if root is None:
            return
        total_sum += root.val
        val_str += '%s,' % root.val
        print(val_str)
        if total_sum == sum and not root.left and not root.right:
            self.result.append([int(v) for v in val_str.split(',') if v])
        if root.left:
            self._dfs(root.left, total_sum, val_str, sum)
        if root.right:
            self._dfs(root.right, total_sum, val_str, sum)


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(-2)
    t4 = TreeNode(-3)
    t5 = TreeNode(5)
    t6 = TreeNode(4)
    t7 = TreeNode(1)
    t3.right = t4
    #t3.right = t5
    #t4.left = t1
    #5.right = t2
    print(s.pathSum(t3, -5))