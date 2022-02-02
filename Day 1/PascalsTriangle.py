class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1],]
        for i in range(1,numRows):
            a=[0]*(i+1)
            a[0]=a[i]=1
            for j in range(1,i):
                a[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(a)
        #print(ans)
        return ans
                