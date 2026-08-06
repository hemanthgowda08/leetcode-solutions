class Solution(object):
    def smallestNumber(self, n, t):
        while True :
            temp = n
            product = 1

            while temp > 0 :
                digit = temp % 10
                product *= digit
                temp //= 10

            if product % t == 0 :
                return n

            n += 1



