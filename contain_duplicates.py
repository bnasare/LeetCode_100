class Solution:
    def containsDuplicate(self, nums):
        seenNum = set()
        for num in nums:
            if num in seenNum:
                return True
            seenNum.add(num)
        return False

nums = [1, 2, 2, 4, 5]

results = Solution().containsDuplicate(nums)
print(results)
