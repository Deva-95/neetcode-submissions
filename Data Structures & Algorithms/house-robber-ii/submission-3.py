class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.hr1(nums[1:]),self.hr1(nums[:-1]))

    def hr1(self,nums):
        rob1,rob2 = 0,0

        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2