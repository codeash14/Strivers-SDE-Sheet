# Moore's Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el,mv=-1,0
        for i in nums:
            el=i if mv==0 else el
            mv+=1 if el==i else -1
        return el if nums.count(el)>len(nums)//2 else -1

#Dict / hashmap approach
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1    
        for i in dict(reversed(sorted(d.items(), key=lambda item: item[1]))):
            if d[i]>(n//2):
                return i
        return -1
'''