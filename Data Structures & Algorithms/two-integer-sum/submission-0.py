class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        i = 0
        while i < len(nums):
            dic[nums[i]] = i
            i += 1
        
        i = 0
        while i < len(dic):
            sec = target - nums[i]
            if sec in dic and dic[sec] != i:
                return [i, dic[sec]]
            i += 1