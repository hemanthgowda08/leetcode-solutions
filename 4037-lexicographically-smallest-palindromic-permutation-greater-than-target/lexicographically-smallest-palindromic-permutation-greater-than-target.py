class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd = [i for i in range(26) if cnt[i] % 2]

        if (n % 2 == 0 and odd) or (n % 2 == 1 and len(odd) != 1):
            return ""

        mid = odd[0] if n % 2 else -1
        half = n // 2
        half_cnt = [c // 2 for c in cnt]

        counts_at = [half_cnt[:]]
        cur = half_cnt[:]
        maxPrefix = 0

        for i in range(half):
            c = ord(target[i]) - 97

            if cur[c] == 0:
                break

            cur[c] -= 1
            counts_at.append(cur[:])
            maxPrefix = i + 1

        def build(prefix, avail):
            rest = []

            for i in range(26):
                rest += [chr(97 + i)] * avail[i]

            full_half = prefix + rest
            suffix = full_half[::-1]

            mid_ch = chr(97 + mid) if mid != -1 else ""

            return "".join(full_half) + mid_ch + "".join(suffix)

        if maxPrefix == half:
            candidate = build(list(target[:half]), [0] * 26)

            if candidate > target:
                return candidate

        for k in range(min(maxPrefix, half - 1), -1, -1):
            avail = counts_at[k][:]
            tc = ord(target[k]) - 97

            chosen = next(
                (c for c in range(tc + 1, 26) if avail[c] > 0),
                -1
            )

            if chosen == -1:
                continue

            avail[chosen] -= 1

            prefix = list(target[:k]) + [chr(97 + chosen)]

            return build(prefix, avail)

        return ""