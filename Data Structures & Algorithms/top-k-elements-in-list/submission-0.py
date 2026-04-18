class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        buckets=[[] for _ in range(n+1)]
        mp=Counter(nums)
        for el,freq in mp.items():
            buckets[freq].append(el)
        res=[]
        for i in range(n,-1,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res)==k:
                    return res
        return res
        