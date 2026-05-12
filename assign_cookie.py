# 455. Assign Cookies
# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# output 有多少 chile 可以被滿足

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        # count 代表有多少 child 可以被滿足
        count = 0
        # i 代表 child 的 index, j 代表 cookie 的 index
        i , j = 0, 0
        while i < len(g) and j < len(s):
            # 如果 cookie 的 size 大於等於 child 的 greed factor, 就可以滿足這個 child
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            # 如果 cookie 的 size 小於 child 的 greed factor, 就不能滿足這個 child, 就換下一個 cookie
            else:
                j += 1