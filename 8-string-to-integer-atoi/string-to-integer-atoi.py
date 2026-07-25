class Solution(object):
    def myAtoi(self, s):
        res = 0
        st = s.strip()
        sign = 1
        int_min = -(2 ** 31)
        int_max = (2 ** 31) - 1

        if len(st) == 0 :
            return 0

        if st[0] == '-' or st[0] == '+' :
            if st[0] == '-':
                sign = -1

            st = st[1:]

    
        for char in st :
            if char.isdigit():
                res = res * 10 + int(char)
            else:
                break

        res = res * sign
        if res < int_min:
            return int_min
        if res > int_max :
            return int_max

        return res