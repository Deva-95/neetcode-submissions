class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            ans = 0
            num = i
            while(num>0):
                ans += num&1
                num = num>>1
            l.append(ans)
        return l