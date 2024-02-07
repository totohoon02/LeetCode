class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        ans = [1] * len(s)
        for i in range(len(s)):
            charSet = set()
            charSet.add(s[i])

            for j in range(i+1, len(s)):
                if(s[j] in charSet): break
                charSet.add(s[j])
                ans[i] += 1

        return max(ans)