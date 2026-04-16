from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            d[tuple(Counter(s)[c] for c in 'abcdefghijklmnopqrstuvxywz')].append(s)

        return list(d.values())
        
        