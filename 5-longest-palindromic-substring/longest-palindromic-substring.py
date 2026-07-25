class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        res_len = 0

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right] :
                if right - left + 1 > res_len :
                    res_len = right - left + 1
                    res = s[left : right + 1]

                left -= 1
                right += 1

        for i in range(len(s)):
            left = i 
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right] :
                if right - left + 1 > res_len :
                    res_len = right - left + 1
                    res = s[left : right + 1]

                left -= 1
                right += 1

        return res


        

        