class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            for digit in str(num):
                if digit == '0' or num % int(digit) != 0:
                    return False
            return True

        result = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)

        return result


# Example usage:
left1, right1 = 1, 22
left2, right2 = 47, 85

solution = Solution()
output1 = solution.selfDividingNumbers(left1, right1)
output2 = solution.selfDividingNumbers(left2, right2)

print("Output 1:", output1)
print("Output 2:", output2)
