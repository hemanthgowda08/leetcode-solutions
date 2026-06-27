from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        freq = Counter(nums)
        ans = 1

        if 1 in freq:
            ans = freq[1] if freq[1] % 2 == 1 else freq[1] - 1

        for x in list(freq.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while freq.get(cur, 0) >= 2:
                length += 2
                cur = cur * cur

            if freq.get(cur, 0) == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans