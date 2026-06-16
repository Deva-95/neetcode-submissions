class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            
            start = i+1
            end = len(nums)-1

            while(start<end):
                s = a + nums[start]+nums[end]
                if s>0:
                    end-=1
                elif s<0:
                    start+=1
                else:
                    res.append([a,nums[start],nums[end]])
                    start+=1
                    while(nums[start]==nums[start-1] and start<end):
                        start+=1
        return res