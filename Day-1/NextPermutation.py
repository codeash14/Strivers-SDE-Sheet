def nextPermutation(nums, n):
    n = len(nums)
    if n <= 2:
        nums.reverse()
        return nums
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        nums.reverse()
        return nums
    for j in range(n - 1, i, -1):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            break
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


#Short code
def nextPermutation(nums, n):
    for i in reversed(range(len(nums) - 1)):
        if nums[i] < nums[i + 1]:
            break
    else:
        nums.reverse()
        return nums
    j = next(j for j in reversed(range(i + 1, len(nums))) if nums[i] < nums[j])
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums
