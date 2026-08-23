class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        if (left_q + right_q) % 2 == 1:
            return True

        diff = left_sum - right_sum

        if left_q > right_q:
            return diff + 9 * (left_q - right_q) // 2 != 0

        if right_q > left_q:
            return diff - 9 * (right_q - left_q) // 2 != 0

        return diff != 0