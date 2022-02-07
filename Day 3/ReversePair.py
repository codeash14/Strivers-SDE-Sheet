class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(beg, end):
            if beg >= end:
                return 0
            mid = (beg + end) // 2
            count = mergeSort(beg, mid) + mergeSort(mid+1, end)
            j = mid + 1
            for i in range(beg, mid + 1):
                while j <= end and nums[i] > 2*nums[j]:
                    j += 1
                count += j-mid-1
            nums[beg:end+1] = sorted(nums[beg:end+1])
            return count
        return mergeSort(0, len(nums) - 1)