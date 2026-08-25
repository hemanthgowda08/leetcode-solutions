class Solution(object):
    def missingMultiple(self, nums, k):
        seen = set(nums)
        mul = k

        while mul in seen :
            mul += k

        return mul

