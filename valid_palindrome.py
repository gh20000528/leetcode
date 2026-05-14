class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 判斷是否為迴文
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        # 如果 s[left] == s[right]，則繼續往內縮小範圍
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)

        return True        