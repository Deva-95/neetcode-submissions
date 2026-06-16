class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_arr = [0]*n
        r_arr = [0]*n
        lp = 1
        rp = 1

        for i in range(n):
            j = -i-1
            l_arr[i]=lp
            r_arr[j]=rp
            lp *= nums[i]
            rp *= nums[j]

        return [i*j for i,j in zip(l_arr,r_arr)]
         