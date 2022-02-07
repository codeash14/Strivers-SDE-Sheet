#using combination
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p=m+n-1
        q=min(m,n)
        num,den=1,1
        for i in range(2,q):
            den*=i
        for i in range(p-q+1,p):
            num*=i
        return num//den
'''
#using dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n]*m
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]
'''