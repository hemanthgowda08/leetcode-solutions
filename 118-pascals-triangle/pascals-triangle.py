class Solution(object):
    def generate(self, numRows):
        n = numRows
        result = []

        for i in range(n):
            if i == 0:
                row = [1]
            else:
                prev = result[-1]
                row = [1]

                for j in range(len(prev) - 1):
                    row.append(prev[j] + prev [j + 1])

                row.append(1)
            
            result.append(row)

        return result