class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        result = []
        n = len(words) - 1
        for i in range(n, -1, -1):
            result.append(words[i])

        return " ".join(result)
