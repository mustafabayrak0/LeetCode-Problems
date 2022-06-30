class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        for i in range (len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    return [i,j]
