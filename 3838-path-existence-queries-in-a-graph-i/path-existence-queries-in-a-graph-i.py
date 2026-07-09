class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        comp = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                comp[i] = comp[i - 1]
            else:
                comp[i] = comp[i - 1] + 1

        answer = []
        for u, v in queries:
            answer.append(comp[u] == comp[v])

        return answer