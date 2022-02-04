class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        p=intervals[0]
        ans=[]
        for i in intervals:
            if (p[0]<=i[0]<=p[1]) or (i[0]<=p[1]<=i[1]):
                p[1]=max(i[1],p[1])
            else:
                #print(p)
                ans.append(p)
                p=i
        ans.append(p)
        return(ans)