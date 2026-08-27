class Solution(object):
    def lexGreaterPermutation(self, s, target):
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        temp = count[:]
        pos = -1

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            for j in range(x + 1, 26):
                if temp[j] > 0:
                    pos = i
                    break

            if temp[x] == 0:
                break

            temp[x] -= 1

        if pos == -1:
            return ""

        for i in range(pos):
            x = ord(target[i]) - ord('a')
            count[x] -= 1

        x = ord(target[pos]) - ord('a')

        for j in range(x + 1, 26):
            if count[j] > 0:
                result = list(target[:pos])
                result.append(chr(j + ord('a')))
                count[j] -= 1

                for k in range(26):
                    result.extend([chr(k + ord('a'))] * count[k])

                return "".join(result)

        return ""