class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]

            i += 1
            j += 1

        ans += word1[i:]
        ans += word2[j:]

        return ans