from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s, k):
        freq = Counter(s)
        n = len(s)
        mid = ""
        half_counts = {}
        for ch, c in freq.items():
            if c % 2:
                mid = ch
            half_counts[ch] = c // 2

        half_len = n // 2
        M = factorial(half_len)
        for c in half_counts.values():
            if c:
                M //= factorial(c)

        if k > M:
            return ""

        counts = dict(half_counts)
        chars = sorted(counts.keys())
        remaining_total = half_len
        result = []

        for _ in range(half_len):
            for ch in chars:
                if counts[ch] == 0:
                    continue
                trial = M * counts[ch] // remaining_total
                if k <= trial:
                    result.append(ch)
                    counts[ch] -= 1
                    M = trial
                    remaining_total -= 1
                    break
                k -= trial

        half = "".join(result)
        return half + mid + half[::-1]