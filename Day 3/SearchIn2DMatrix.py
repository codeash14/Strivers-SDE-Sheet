class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k=-1
        for i in matrix:
            if target < i[0]:
                break
            k+=1
        
        if target in matrix[k]:
            return True
        return False

#Alternative Approach
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        beg,end=0,(m*n)-1
        while(end>=beg):
            mid=beg+(end-beg)//2
            if matrix[mid//n][mid%n]==target:
                return True
            if matrix[mid//n][mid%n]<target:
                beg=mid+1
            else:
                end=mid-1
        return False
'''