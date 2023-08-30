from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        results = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            results[tuple(count)].append(word)

        return list(results.values())

# Example usage
str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
result = solution.groupAnagrams(str_list)
print(result)
