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
        p,q=0,len(matrix)-1
        while(q>=p):
            mid=p+(q-p)//2
            #print(mid)
            if target in matrix[mid]:
                return True
            elif target<matrix[mid][0]:
                q=mid-1
            else:
                p=mid+1
            
        return False
'''