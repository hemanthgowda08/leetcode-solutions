class Solution(object):
    def findContentChildren(self, g, s):
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        count = 0
        left = 0
        right = 0

        while left < n and right < m :
            if g[left] <= s[right] :
                count += 1
                left += 1
                right += 1
            else :
                right += 1

        return count
