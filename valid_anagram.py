# 242. Valid Anagram
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果兩字串長度不一樣 return false
        if len(s) != len(t):
            return False

        # 排序兩個字串
        s_sort = sorted(s)
        t_sort = sorted(t)

        # 比對兩個字串的每個字母是否相同
        for i in range(len(s_sort)):
            if s_sort[i] != t_sort[i]:
                return False

        return True