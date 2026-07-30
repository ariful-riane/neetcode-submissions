class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums)//2]

        left = [n for n in nums if n < pivot]
        mid = [n for n in nums if n == pivot]
        right = [n for n in nums if n > pivot]

        return self.sortArray(left) + mid + self.sortArray(right)