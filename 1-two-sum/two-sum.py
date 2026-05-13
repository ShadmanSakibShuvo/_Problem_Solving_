class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in dic:
                return [dic[value], i]
            dic[num] = i