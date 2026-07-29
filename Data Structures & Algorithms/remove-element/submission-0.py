class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            else:
                nums[i] = '_'
                count += 1
        return len(nums) - count