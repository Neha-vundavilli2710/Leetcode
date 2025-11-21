class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1]*26
        last = [-1]*26
        n = len(s)

        for i, c in enumerate(s):
            idx = ord(c) - 97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0
        for ch in range(26):
            if first[ch] != -1 and last[ch] > first[ch]:
                seen = set()
                for i in range(first[ch] + 1, last[ch]):
                    seen.add(s[i])
                ans += len(seen)

        return ans
