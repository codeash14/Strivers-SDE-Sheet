class Solution:
    def myPow(self, x: float, n: int) -> float:
        m=abs(n)
        ans=1.0
        while m!=0:
            if m%2==0:
                x=x*x
                m=m//2
            else:
                ans=ans*x
                m-=1
        return ans if n>0 else 1/ans