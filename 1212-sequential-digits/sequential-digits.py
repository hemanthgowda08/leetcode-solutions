class Solution(object):
    def sequentialDigits(self, low, high):
        digits = "123456789"
        ans = []

        low_len = len(str(low))
        high_len = len(str(high))

        for length in range(low_len, high_len + 1):

            for start in range(10 - length):
                num = int(digits[start:start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans