class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d = defaultdict(int)
        e = defaultdict(int)
        for i in range(len(s)):
            d[s[i]]+=1
            e[t[i]]+=1
        for char in t:
            if e[char]!=d[char]:
                return False
        return True