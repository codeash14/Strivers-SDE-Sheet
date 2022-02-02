class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums)-1

        while w <= b:
            if nums[w] == 0:  #swap with r-th index if 0 occurs at w-th index
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            elif nums[w] == 1:
                w += 1
            else:             #swap with b-th index if 2 occurs at w-th index
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1    