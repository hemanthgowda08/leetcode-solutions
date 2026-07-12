class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr))

        rank = {}

        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1
            
        ans = []

        for num in arr :
            ans.append(rank[num])
        return ans
