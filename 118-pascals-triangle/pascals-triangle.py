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
                for j in range(1, i):
                    row.append(prev[j-1] + prev[j])

                row.append(1)
            result.append(row)
        return result
    
print(Solution().generate(5))