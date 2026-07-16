class Solution(object):
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefixGcd = []
        mx = 0

        for num in nums:
            if num > mx:
                mx = num
            prefixGcd.append(gcd(num, mx))

        prefixGcd.sort()

        ans = 0
        i = 0
        j = len(prefixGcd) - 1

        while i < j:
            ans += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans