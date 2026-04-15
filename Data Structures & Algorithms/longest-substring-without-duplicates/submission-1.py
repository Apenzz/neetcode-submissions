class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        r = 0
        for l in range(len(s)):
            while s[l] in s[r:l]:
                r += 1
            else:
                maxLen = max(maxLen, len(s[r:l])+1)
        return maxLen
