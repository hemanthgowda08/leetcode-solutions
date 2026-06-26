class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        arr = [1 if x == target else -1 for x in nums]

        prefix = [0]
        s = 0
        for x in arr:
            s += x
            prefix.append(s)

        values = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(values)}

        bit = [0] * (len(values) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0

        for p in prefix:
            idx = rank[p]
            ans += query(idx - 1)
            update(idx)

        return ans