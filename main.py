def setMatrixOnes(MAT, n, m):
    cnt=0
    for i in range(1,n):
        if MAT[0][i]==1:
            cnt=1
        for j in range(1,m):
            if MAT[i][j]==1:
                MAT[i][0]=1
                MAT[0][j]=1
    for i in range(n-1,0,-1):
        for j in range(m-1,0,-1):
            if MAT[i][0]==1 or MAT[0][j]==1:
                MAT[i][j]==1
        if cnt==1:
            MAT[i][0]=1