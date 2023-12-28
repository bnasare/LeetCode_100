class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        merged = ""

        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]  # Merge characters alternately
            i += 1
            j += 1

        # Append any remaining characters from the longer word
        merged += word1[i:] + word2[j:]

        return merged
