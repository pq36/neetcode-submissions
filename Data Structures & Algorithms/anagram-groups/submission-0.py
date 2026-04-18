class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        hlst=[[0]*26 for _ in range(n)]
        res=defaultdict(list)
        for ind,i in enumerate(strs):
            for j in i:
                hlst[ind][ord(j)-ord('a')]+=1
            res[tuple(hlst[ind])].append(i)
        return list(res.values())

        