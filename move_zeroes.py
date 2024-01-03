class Solution(object):
    def moveZeroes(self, nums):
        non_zero_index = 0
        for num in nums:
            if num != 0:
                nums[non_zero_index] = num
                non_zero_index += 1
        nums[non_zero_index:] = [0] * (len(nums) - non_zero_index)
