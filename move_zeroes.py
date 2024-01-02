class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize a variable to keep track of the position to insert non-zero elements
        non_zero_index = 0

        # Iterate through the array
        for num in nums:
            if num != 0:
                # If the current element is non-zero, move it to the non_zero_index position
                nums[non_zero_index] = num
                non_zero_index += 1

        # Fill the remaining positions with zeros
        while non_zero_index < len(nums):
            nums[non_zero_index] = 0
            non_zero_index += 1
