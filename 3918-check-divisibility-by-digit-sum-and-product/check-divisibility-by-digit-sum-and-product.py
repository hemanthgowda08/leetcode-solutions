class Solution(object):
    def checkDivisibility(self, n):
        add = 0
        prod = 1
        temp = n
        while temp > 0 :
            d = temp % 10
            add += d
            prod *= d
            temp //= 10
        total = add + prod
        return n % total == 0