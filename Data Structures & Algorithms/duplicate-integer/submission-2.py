class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         d = defaultdict(int)
         for x in nums:
            d[x]+=1
            if d[x]>1:
                return True
         return False