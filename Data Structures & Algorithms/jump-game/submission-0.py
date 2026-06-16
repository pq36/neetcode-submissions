class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0
        for ind,num in enumerate(nums):
            if ind>max_jump:
                return False
            max_jump=max(max_jump,ind+num)
        return True
        