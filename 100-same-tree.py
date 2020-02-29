# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q) -> bool:
        p_arr = self.tree_arr(p)
        q_arr = self.tree_arr(q)
        if len(p_arr) != len(q_arr):
            return False
        for i in range(len(p_arr)):
            p_val = p_arr[i].val if p_arr[i] else None
            q_val = q_arr[i].val if q_arr[i] else None
            if p_val != q_val:
                return False
        return True

    def tree_arr(self, p):
        if not p: return []
        arr = [p]
        for node in arr:
            if not node:
                continue
            if node.left:
                arr.append(node.left)
            else:
                arr.append(None)
            if node.right:
                arr.append(node.right)
            else:
                arr.append(None)
        return arr


if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    print(solution.isSameTree(t1, t2))