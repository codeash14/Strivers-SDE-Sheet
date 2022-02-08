def rotateMatrix(mat, n, m):
    top, down, left, right = 0, n, 0, m

    while (left < right and top < down):
        if top + 1 == down or left + 1 == right:
            break
        nxt = mat[top + 1][left]
        #left to right
        for i in range(left, right):
            mat[top][i], nxt = nxt, mat[top][i]
        top += 1

        #top to down
        for i in range(top, down):
            mat[i][right - 1], nxt = nxt, mat[i][right - 1]
        right -= 1

        if top < down:
            #right to left
            for i in range(right - 1, left - 1, -1):
                mat[down - 1][i], nxt = nxt, mat[down - 1][i]
        down -= 1

        if left < right:
            #down to top
            for i in range(down - 1, top - 1, -1):
                mat[i][left], nxt = nxt, mat[i][left]
        left += 1
