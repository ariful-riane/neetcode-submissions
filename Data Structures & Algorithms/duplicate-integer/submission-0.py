class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for i in range(len(nums)):
            dup.add(nums[i])
        return len(nums) != len(dup)
 