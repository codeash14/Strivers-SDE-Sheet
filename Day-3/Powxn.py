import sys

sys.setrecursionlimit(10**7)


def modularExponentiation(x, n, m):
    n1 = abs(n)
    ans = 1
    while n1 != 0:
        if n1 % 2 == 0:
            x = (x % m) * (x % m)
            n1 //= 2
        else:
            ans = (ans % m) * (x % m)
            n1 -= 1

    return ans % m


# Main.
t = int(input())
while (t > 0):
    lst = list(map(int, input().split()))
    x, n, m = lst[0], lst[1], lst[2]
    print(modularExponentiation(x, n, m))
    t -= 1
