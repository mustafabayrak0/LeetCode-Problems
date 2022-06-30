class Solution:
    @staticmethod
    def sortColors(nums):
        lst = []
        while len(nums) != 0:
            minx = nums[0]
            for i in nums:
                if i < minx:
                    minx = i
            lst.append(minx)
            nums.remove(minx)
        for i in range(len(lst)):
            nums.append(lst[i])
        return nums
