class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        pxor=0
        for i in range(1,n+1):
            pxor^=i
        for i in nums:
            pxor^=i
        return pxor


        