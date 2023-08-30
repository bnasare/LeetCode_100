from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        # Compare the Counter of characters in s and t
        return Counter(s) == Counter(t)

# Example usage
solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t))  # Output: True