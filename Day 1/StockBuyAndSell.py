class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        proffit=0
        for i in prices:
            mini=min(i,mini)
            proffit=max(proffit,i-mini)
        return proffit