class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        diff = len(nums) - len(set(nums)) 
        summ = sum(nums) - sum(set(nums))
        return summ//diff