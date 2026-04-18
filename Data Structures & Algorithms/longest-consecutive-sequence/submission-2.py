class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        maxi=0
        for i in st:
            if i-1 not in st:
                cnt=1
                while i+cnt in st:
                    cnt+=1
                maxi=max(cnt,maxi)
       
        return maxi
            
            
        