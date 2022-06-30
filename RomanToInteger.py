class Solution(object):
    @staticmethod
    def productExceptSelf(nums):
        lst = []
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary.keys():
                mul = dictionary[nums[i]]
            else:
                mul = 1
                k = nums[i]
                nums[i] = 1
                for j in range(len(nums)):
                    mul *= nums[j]
                    if nums[j] == 0:
                        break
                        mul = 0
                nums[i] = k
                dictionary[nums[i]] = mul
            lst.append(int(mul))
        return lst
