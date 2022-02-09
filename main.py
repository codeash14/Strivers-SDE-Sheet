def subarraysXor(arr, x):
    cnt = xor = 0
    d = {}
    for i in arr:
        xor = xor ^ i
        if xor == x:
            cnt += 1
        if xor ^ x in d:
            cnt += d[xor ^ x]
        if xor in d:
            d[xor] += 1
        else:
            d[xor] = 1
    return cnt
