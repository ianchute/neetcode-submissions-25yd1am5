class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a, b, n = 0, 1, len(s)
        best = min(n, 1)
        while a < b <= n:
            chunk = s[a:b]
            uniq = len(set(chunk)) == len(chunk)
            if not uniq:
                a += 1
            else:
                print(s[a:b])
                best = max(best, b - a)
            b += 1
        return best