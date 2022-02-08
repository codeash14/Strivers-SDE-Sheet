from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


class Solution:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def mergeIntervals(intervals):
    p = intervals[0]
    ans = []
    for i in intervals:
        if (p.start <= i.start <= p.end) or (i.start <= p.end <= i.end):
            p.end = max(i.end, p.end)
        else:
            ans.append(p)
            p = i
    ans.append(p)
    return (ans)


n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
