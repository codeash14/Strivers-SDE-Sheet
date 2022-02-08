#approach 1
def findTargetInMatrix(mat, m, n, target):
    k = -1
    for i in mat:
        if target < i[0]:
            break
        k += 1

    if target in mat[k]:
        return True
    return False


#approach 2
def findTargetInMatrix(matrix, m, n, target):
    beg, end = 0, (m * n) - 1
    while (end >= beg):
        mid = beg + (end - beg) // 2
        if matrix[mid // n][mid % n] == target:
            return True
        if matrix[mid // n][mid % n] < target:
            beg = mid + 1
        else:
            end = mid - 1
    return False
