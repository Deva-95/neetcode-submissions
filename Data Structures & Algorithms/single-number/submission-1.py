class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = 0
        for x in nums:
            val ^=x
        return val