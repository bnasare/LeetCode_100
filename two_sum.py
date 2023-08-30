class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}  # Create a dictionary to store previously seen numbers and their indices
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i  # Store the current number in the dictionary with its index

# Example usage
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # This should print [0, 1] because nums[0] + nums[1] equals the target 9
