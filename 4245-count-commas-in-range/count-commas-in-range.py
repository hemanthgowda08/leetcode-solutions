class Solution(object):
    def countCommas(self, n):
        count = 0

        if n < 1000 :
            return 0
        
        for i in range(1000, n + 1) :
            digits = len(str(i))
            count += (digits - 1) // 3

        return count