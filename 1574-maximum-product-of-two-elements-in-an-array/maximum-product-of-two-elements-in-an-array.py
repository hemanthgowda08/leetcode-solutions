class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        large = nums[-1]
        second = nums[-2]
        return (large - 1) * (second - 1)
        