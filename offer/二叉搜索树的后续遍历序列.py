'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false
示例 2：
输入: [1,3,2,6,5]
输出: true
'''


class Solution:

    def verifyPostorder(self, postorder):
        if not postorder: return False
        return self.check(postorder, 0, len(postorder)-1)

    def check(self, postorder, first, last):
        if last - first <= 1:
            return True
        root = postorder[last]
        index = first
        while first < last and postorder[index] < root:
            index += 1
        for i in range(index, last):
            if postorder[i] < root:
                return False
        return self.check(postorder, index, last-1) and self.check(postorder, first, index-1)


if __name__ == '__main__':
    s = Solution()
    print(s.verifyPostorder([1,6,3,2,5]))