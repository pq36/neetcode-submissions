class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        res=0
        for i in prices:
            if i<mini:
                mini=i
            res=max(i-mini,res)
        return res

        