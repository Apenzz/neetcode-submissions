from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        # create hash table
        char_dict = Counter(s1)
        # sliding window over s2 to find permutation
        r, l = 0, len(s1)
        sub_dict = Counter(s2[r:l])
        while l <= len(s2):
            if (char_dict == sub_dict):
                return True
            sub_dict[s2[r]] -= 1
            if l < len(s2):
                sub_dict[s2[l]] += 1
            r += 1
            l += 1
        return False

        