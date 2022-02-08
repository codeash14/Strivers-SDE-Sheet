# Modified moore's voting algorithm
def majorityElementII(arr):
    el1, c1, el2, c2 = -1, 0, -1, 0
    for i in arr:
        if i == el1:
            c1 += 1
        elif i == el2:
            c2 += 1
        elif c1 == 0:
            c1 += 1
            el1 = i
        elif c2 == 0:
            c2 += 1
            el2 = i
        else:
            c1 -= 1
            c2 -= 1
    ans = []
    if c1 > 0 and arr.count(el1) > len(arr) // 3:
        ans.append(el1)
    if c2 > 0 and arr.count(el2) > len(arr) // 3:
        ans.append(el2)
    return ans


# dict/hash map approach
def majorityElementII(arr):
    d = {}
    for i in arr:
        d[i] = 1 if i not in d else d[i] + 1
    ans = []
    for i in d:
        if d[i] > len(arr) // 3:
            ans.append(i)
    return ans
