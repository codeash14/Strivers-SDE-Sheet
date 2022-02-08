#using combination (for 100 marks)
def uniquePaths(m, n):
    p, q = m + n - 1, min(m, n)
    num, den = 1, 1
    for i in range(2, q):
        den *= i
    for j in range(p - q + 1, p):
        num *= j
    return num // den


#using dp (for 91 marks)
def uniquePaths(m, n):
    dp = [[1] * n] * m
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
