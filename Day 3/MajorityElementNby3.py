# Modified moore's voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1,el2=-1,-1
        c1,c2=0,0
        for i in nums:
            if i==el1:
                c1+=1
            elif i==el2:
                c2+=1
            elif c1==0:
                el1=i
                c1+=1
            elif c2==0:
                el2=i
                c2+=1
            else:
                c1-=1
                c2-=1
        ans=[]
        if c1>0 and nums.count(el1)>len(nums)//3:
            ans.append(el1)
        if c2>0 and nums.count(el2)>len(nums)//3:
            ans.append(el2)
        return ans
            
        


# dict/hash map approach
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=1 if i not in d else d[i]+1   
        ans=[]
        for i in d:
            if d[i]>len(nums)//3:
                ans.append(i)
        return ans
'''