class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        missing = (n*(n+1)//2) - sum(set(A)) 
        repeating = sum(A) - sum(set(A))
        return repeating,missing
