class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d = {}
        e = {}
        for i in range(len(s)):
            d[s[i]]=1+d.get(s[i],0)
            e[t[i]]=1+e.get(t[i],0)
        for char in t:
            if e[char]!=d.get(char,0):
                return False
        return True