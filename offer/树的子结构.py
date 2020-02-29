# Definition for a binary tree node.
'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B) -> bool:
        if not A and not B:
            return False
        if not A or not B:
            return False
        if self.isEqual(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isEqual(self, A, B):
        if not B:
            return True
        if not A:
            return False
        return A.val == B.val and self.isEqual(A.left, B.left) and self.isEqual(A.right, B.right)


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
    t4.right = t2
    t6.left = t7
    print(s.isSubStructure(t3, t6))