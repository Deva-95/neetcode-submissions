class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = set()
        for x in nums:
            if x not in n:
                n.add(x)
            else:
                return x