
class Solution(object):
    """
    替换数组中的某一个字符为其他多个字符
    O(n)
    """

    def replace_blank(self, world, target='a', replace='abc'):
        p1 = len(world) - 1
        count = 0
        for w in world:
            if w == 'a':
                count += 1
        new_len = len(world) + count*len(replace) - len(target)*count
        world_new = [0] * new_len
        p2 = new_len - 1
        while p1 > -1:
            if world[p1] != 'a':
                world_new[p2] = world[p1]
                p1 -= 1
                p2 -= 1
            else:
                for r in replace:
                    world_new[p2] = r
                    p2 -= 1
                for t in target:
                    p1 -= 1
        return world_new


if __name__ == '__main__':
    print(Solution().replace_blank([1, 2, 3, 'a', 4, 5, 'a', 6], 'a', 'abc'))
