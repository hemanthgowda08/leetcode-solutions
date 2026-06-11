class Solution(object):
    def reverse(self, x):
        rev = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x


        while x != 0:
            d = x % 10
            rev = rev * 10 + d
            x = x // 10

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        

        return rev * sign