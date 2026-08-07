class Solution:
    def smallestNumber(self, num, t):
        kFactorCounts = {
            0: {}, 1: {}, 2: {2: 1}, 3: {3: 1}, 4: {2: 2},
            5: {5: 1}, 6: {2: 1, 3: 1}, 7: {7: 1}, 8: {2: 3}, 9: {3: 2}
        }

        def getPrimeCount(t):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in (2, 3, 5, 7):
                while t % p == 0:
                    t //= p
                    count[p] += 1
            return count, t == 1

        def getPrimeCountFromString(s):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for ch in s:
                for p, e in kFactorCounts[int(ch)].items():
                    count[p] += e
            return count

        def getFactorCount(count):
            count8 = count[2] // 3
            remaining2 = count[2] % 3
            count9 = count[3] // 2
            count3 = count[3] % 2
            count4 = remaining2 // 2
            count2 = remaining2 % 2
            count6 = 0
            if count2 == 1 and count3 == 1:
                count2, count3, count6 = 0, 0, 1
            if count3 == 1 and count4 == 1:
                count2, count6, count3, count4 = 1, 1, 0, 0
            return {2: count2, 3: count3, 4: count4, 5: count[5],
                    6: count6, 7: count[7], 8: count8, 9: count9}

        def construct(factors):
            return "".join(str(d) * factors.get(d, 0) for d in range(2, 10))

        def isSubset(a, b):
            return all(b.get(k, 0) >= v for k, v in a.items())

        def subtract(a, b):
            res = dict(a)
            for k, v in b.items():
                res[k] = max(0, res.get(k, 0) - v)
            return res

        def sumValues(count):
            return sum(count.values())

        primeCount, isDivisible = getPrimeCount(t)
        if not isDivisible:
            return "-1"

        factorCount = getFactorCount(primeCount)
        if sumValues(factorCount) > len(num):
            return construct(factorCount)

        primeCountPrefix = getPrimeCountFromString(num)
        firstZeroIndex = num.find('0')
        if firstZeroIndex == -1:
            firstZeroIndex = len(num)
            if isSubset(primeCount, primeCountPrefix):
                return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            primeCountPrefix = subtract(primeCountPrefix, kFactorCounts[d])
            spaceAfterThisDigit = len(num) - 1 - i
            if i > firstZeroIndex:
                continue
            for biggerDigit in range(d + 1, 10):
                factorsAfterReplacement = getFactorCount(
                    subtract(subtract(primeCount, primeCountPrefix), kFactorCounts[biggerDigit])
                )
                if sumValues(factorsAfterReplacement) <= spaceAfterThisDigit:
                    fillOnes = spaceAfterThisDigit - sumValues(factorsAfterReplacement)
                    return num[:i] + str(biggerDigit) + "1" * fillOnes + construct(factorsAfterReplacement)

        factorsAfterExtension = getFactorCount(primeCount)
        return "1" * (len(num) + 1 - sumValues(factorsAfterExtension)) + construct(factorsAfterExtension)