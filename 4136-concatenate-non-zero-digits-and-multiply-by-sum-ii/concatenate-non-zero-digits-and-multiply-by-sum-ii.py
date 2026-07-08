class Solution(object):
    def sumAndMultiply(self, param_1, param_2):
        s = param_1
        queries = param_2

        MOD = 10**9 + 7
        n = len(s)

        cnt = [0] * (n + 1)
        filtered = []
        for i, ch in enumerate(s):
            d = int(ch)
            cnt[i + 1] = cnt[i] + (1 if d != 0 else 0)
            if d != 0:
                filtered.append(d)

        k = len(filtered)
        V = [0] * (k + 1)
        sumPrefix = [0] * (k + 1)
        pow10 = [1] * (k + 1)

        for i in range(k):
            V[i + 1] = (V[i] * 10 + filtered[i]) % MOD
            sumPrefix[i + 1] = sumPrefix[i] + filtered[i]
            pow10[i + 1] = (pow10[i] * 10) % MOD

        answer = []
        for l, r in queries:
            a = cnt[l]
            b = cnt[r + 1]

            if b <= a:
                answer.append(0)
                continue

            length = b - a
            x_val = (V[b] - V[a] * pow10[length]) % MOD
            x_val = (x_val + MOD) % MOD

            digit_sum = sumPrefix[b] - sumPrefix[a]

            answer.append((x_val * (digit_sum % MOD)) % MOD)

        return answer