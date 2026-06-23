class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=0
        for ind, val in enumerate(nums):
            if ind>max_reach:
                return False
            max_reach=max(max_reach,ind+val)
        return True
        