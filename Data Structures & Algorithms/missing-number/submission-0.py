class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        for i in nums:
            x1 ^= i
        for j in range(len(nums)+1):
            x2 ^= j
        ans = x1 ^ x2
        return ans