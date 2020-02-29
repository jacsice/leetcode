'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        visited = set()
        start = 0
        max_count = 0
        cur_count = 0
        for index, c in enumerate(s):
            cur_count += 1
            while c in visited:
                visited.remove(s[start])
                start += 1
                cur_count -= 1
            visited.add(c)
            max_count = max(max_count, cur_count)
        return max_count


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('bbbbb'))