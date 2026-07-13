class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            total = 0

            while num > 0:
                digit = num % 10
                total += digit
                num //= 10

            num = total

        return num