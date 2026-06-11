class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0

        while x > rev :
            d = x % 10
            rev = rev * 10 + d
            x //= 10

        return x == rev or x == rev // 10