class Solution:
    def minWindow(self, s: str, t: str) -> str:
        comp=Counter(t)
        mp=defaultdict(int)
        resr=float('inf')
        resl=0
        l=0
        for r in range(len(s)):
            mp[s[r]]+=1
            while l < len(s) and (s[l] not in comp or mp[s[l]] > comp[s[l]]):
                mp[s[l]]-=1
                l+=1
            flg=True
            for i in comp.keys():
                if mp[i]<comp[i]:
                    flg=False
            if flg and ((resr-resl) > (r-l)):
                resr=r
                resl=l
        if resr==float('inf'):
            return ''
        return s[resl:resr+1]