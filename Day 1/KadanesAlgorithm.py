from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


def maxSubarraySum(nums, n):
    result = 0
    s = 0
    for i in nums:
        s += i
        result = max(result, s)
        if (s < 0):
            s = 0
    return result


#taking input using fast I/O
def takeInput():

    n = int(input())

    if (n == 0):
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
