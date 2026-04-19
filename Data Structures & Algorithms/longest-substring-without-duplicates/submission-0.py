class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=defaultdict(int)
        n=len(s)
        l=0
        maxi=0
        for r in range(n):
            while mp[s[r]]:
                mp[s[l]]-=1
                l+=1
            mp[s[r]]+=1
            maxi=max(maxi,r-l+1)
        return maxi
            
        