from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


def sort012(arr, n):
    r, w, b = 0, 0, n - 1

    while w <= b:
        if arr[w] == 0:  #swap with r-th index if 0 occurs at w-th index
            arr[r], arr[w] = arr[w], arr[r]
            w += 1
            r += 1
        elif arr[w] == 1:
            w += 1
        else:  #swap with b-th index if 2 occurs at w-th index
            arr[w], arr[b] = arr[b], arr[w]
            b -= 1


#taking input using fast I/O
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


def printAnswer(arr, n):

    for i in range(n):

        print(arr[i], end=" ")

    print()


#main

t = int(input().strip())
for i in range(t):

    arr, n = takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
