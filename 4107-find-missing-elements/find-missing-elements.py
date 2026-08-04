class Solution(object):
    def findMissingElements(self, nums):
        s = set(nums)
        small = min(nums)
        largest = max(nums)
        res = []
        for i in range(small,largest + 1):
            if i not in s :
                res.append(i)
        return res

