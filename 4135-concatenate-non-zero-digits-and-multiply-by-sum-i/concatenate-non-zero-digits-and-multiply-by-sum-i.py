class Solution(object):
    def sumAndMultiply(self, n):
        x = 0
        sum_digit = 0

        for digit in str(n):
            if digit != '0' :
                x = x * 10 + int(digit)
                sum_digit += int(digit)

        return x * sum_digit
