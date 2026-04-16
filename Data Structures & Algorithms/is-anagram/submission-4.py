
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        char_freq = {c : 0 for c in alphabet}

        for c in s:
            char_freq[c] += 1
        for c in t:
            char_freq[c] -= 1
        return all(v == 0 for v in char_freq.values())