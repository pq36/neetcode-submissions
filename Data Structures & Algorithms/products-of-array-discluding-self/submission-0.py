class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=[1]*n
        suf=[1]*n
        prod=nums[0]
        for i in range(1,n):
            pref[i]=prod
            prod*=nums[i]
        prod=nums[n-1]
        res=[1]*n
        for i in range(n-2,-1,-1):
            suf[i]=prod
            prod*=nums[i]
            res[i]=pref[i]*suf[i]
        res[0]=suf[0]
        res[n-1]=pref[n-1]
        return res



        