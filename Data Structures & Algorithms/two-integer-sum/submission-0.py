class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp=defaultdict()
        for ind,i in enumerate(nums):
            if target-i in mp:
                return [mp[target-i],ind]
            mp[i]=ind
        return []