# Moore's Voting Algorithm
def findMajorityElement(arr, n):
    el, mv = -1, 0
    for i in arr:
        el = i if mv == 0 else el
        mv += 1 if el == i else -1
    return el if arr.count(el) > n // 2 else -1


#Dict / hashmap approach
def findMajorityElement(arr, n):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in dict(reversed(sorted(d.items(), key=lambda item: item[1]))):
        if d[i] > (n // 2):
            return i
    return -1
