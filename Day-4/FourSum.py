def fourSum(arr, target):
    arr.sort()
    ans = kSum(arr, target, 4)
    return "Yes" if ans else "No"


def kSum(arr, target, k):
    res = []
    if not arr:
        return res
    avg = target // k
    if avg < arr[0] or arr[-1] < avg:
        return res
    if k == 2:
        return twoSum(arr, target)
    for i in range(len(arr)):
        if i == 0 or arr[i - 1] != arr[i]:
            for subset in kSum(arr[i + 1:], target - arr[i], k - 1):
                res.append([arr[i]] + subset)
    return res


def twoSum(arr, target):
    res = []
    s = set()
    for i in range(len(arr)):
        if len(res) == 0 or res[-1][1] != arr[i]:
            if target - arr[i] in s:
                res.append([target - arr[i], arr[i]])
        s.add(arr[i])
    return res
