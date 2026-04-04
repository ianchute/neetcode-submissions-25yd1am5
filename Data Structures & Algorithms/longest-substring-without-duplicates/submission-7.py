class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a, b, n = 0, 1, len(s)
        if n == 0: return 0
        if n == 1: return 1
        best = 1
        while a < b <= n:
            chunk = s[a:b]
            uniq = len(set(chunk)) == len(chunk)
            if not uniq:
                a += 1
            else:
                best = max(best, b - a)
            b += 1
        return best