class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        frequency = {}

        for num in nums:
            count += frequency.get(num, 0)
            frequency[num] = frequency.get(num, 0) + 1

        return count
