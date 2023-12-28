class Solution(object):
    def smallestCommonMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 0:
            # If n is already even, then it is the smallest positive integer that is a multiple of both 2 and n.
            return n
        else:
            # If n is odd, then the smallest positive integer that is a multiple of both 2 and n is 2n.
            return n * 2
