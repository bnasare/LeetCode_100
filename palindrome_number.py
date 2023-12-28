class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):  # Handle negative and trailing zeros cases
            return False

        reversedNum = 0
        originalNum = x

        while x > 0:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10

        return reversedNum == originalNum
